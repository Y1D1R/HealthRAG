"""
This is the setup script for the HealthRAG project.
"""

from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="HealthRAG",
    version="0.1.0",
    author="Yidhir",
    description="""HealthRAG is a Retrieval-Augmented Generation (RAG)
    chatbot designed for medical document question-answering""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
)
