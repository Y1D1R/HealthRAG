from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="HealthRAG",
    version="0.1.0",
    author="Yidhir",
    description="HealthRAG is a Retrieval-Augmented Generation (RAG) chatbot designed for medical document question-answering",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
)