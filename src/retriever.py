from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama

from config import VECTOR_DB_DIR, TOP_K


def ask(question: str) -> str:
    # Embeddings locales
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # Base vectorial
    db = Chroma(
        persist_directory=str(VECTOR_DB_DIR),
        embedding_function=embeddings,
    )

    # Recuperar contexto
    docs = db.similarity_search(question, k=TOP_K)

    if not docs:
        return "No se encontró información relevante."

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
Responde únicamente con la información del contexto.
Si no encuentras la respuesta, responde:
'No existe suficiente información en los documentos.'

Contexto:
{context}

Pregunta:
{question}
"""

    # Modelo local con Ollama
    llm = ChatOllama(
        model="llama3",
        temperature=0
    )

    response = llm.invoke(prompt)
    return response.content


if __name__ == "__main__":
    question = input("Pregunta: ")
    print("\nRespuesta:\n")
    print(ask(question))