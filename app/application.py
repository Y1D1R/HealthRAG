from flask import Flask,render_template,request,session,redirect,url_for
from app.components.retriever import create_retrieval_qa_chain
from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.environ.get("HF_TOKEN")

app = Flask(__name__)
app.secret_key = os.urandom(24)

from markupsafe import Markup
def nl2br(value):
    return Markup(value.replace("\n" , "<br>\n"))

app.jinja_env.filters['nl2br'] = nl2br

@app.route("/" , methods=["GET","POST"])
def index():
    if "messages" not in session:
        session["messages"]=[]

    if request.method=="POST":
        user_input = request.form.get("prompt")

        if user_input:
            messages = session["messages"]
            messages.append({"role" : "user" , "content":user_input})
            session["messages"] = messages

            try:
                vector_store, llm = create_retrieval_qa_chain()

                # contexte
                context_docs = vector_store.similarity_search(user_input, k=1)
                context = "\n".join([doc.page_content for doc in context_docs])

                # Prompt
                custom_prompt = f"""
                You are a professional medical assistant. You must reply concisely and directly to the user's question using only the context.

                ⚠️ Do NOT explain your thought process.  
                ⚠️ Do NOT analyze the question or the context.  
                ⚠️ Do NOT repeat the question.  
                ⚠️ Do NOT mention what you can or cannot do.  
                ⚠️ DO NOT say things like "the user is asking..." or "the context says..."

                Respond in **2 to 3 complete sentences** ONLY, and provide the answer **based purely on the context**.

                Context:
                {context}

                Question:
                {user_input}

                Answer:
                """

                raw_response = llm.invoke(custom_prompt)
                
                #print(f"Raw response from LLM: {raw_response}")
                if "</think>" in raw_response:
                    final_answer = raw_response.split("</think>")[-1].strip()
                else:
                    final_answer = raw_response.strip()

                messages.append({"role": "assistant", "content": final_answer})
                session["messages"] = messages

            except Exception as e:
                error_msg = f"Error : {str(e)}"
                return render_template("index.html" , messages = session["messages"] , error = error_msg)
            
        return redirect(url_for("index"))
    return render_template("index.html" , messages=session.get("messages" , []))

@app.route("/clear")
def clear():
    session.pop("messages" , None)
    return redirect(url_for("index"))

if __name__=="__main__":
    app.run(host="0.0.0.0" , port=5000 , debug=False , use_reloader = False)



