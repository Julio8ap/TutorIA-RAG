from pathlib import Path

from langchain_community.document_loaders import (
    PyMuPDFLoader,
    TextLoader,
)
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from config import (
    DATA_DIR,
    VECTOR_DB_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


def load_documents():
    """Carga todos los documentos de la carpeta data/."""
    documents = []

    for file in DATA_DIR.iterdir():
        print(f"Leyendo: {file.name}")

        if file.suffix.lower() == ".pdf":
            loader = PyMuPDFLoader(str(file))
        else:
            loader = TextLoader(str(file), encoding="utf-8")

        documents.extend(loader.load())

    return documents


def main():
    try:
        print("Cargando documentos...")
        docs = load_documents()
        print(f"Documentos cargados: {len(docs)}")

        print("Dividiendo documentos en fragmentos...")
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )
        chunks = splitter.split_documents(docs)
        print(f"Fragmentos generados: {len(chunks)}")

        print("Generando embeddings...")
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        print("Guardando embeddings en ChromaDB...")
        Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=str(VECTOR_DB_DIR),
        )

        print("Indexación completada exitosamente.")

    except Exception as e:
        print(f"Error durante la indexación: {e}")


if __name__ == "__main__":
    main()