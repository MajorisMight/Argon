from langchain_community.vectorstores import FAISS
from retrieval.embeddings import embeddings


def create_vector_store(documents):

    db = FAISS.from_documents(
        documents,
        embeddings
    )

    db.save_local("vector_store")


def load_vector_store():

    return FAISS.load_local(
        "vector_store",
        embeddings,
        allow_dangerous_deserialization=True
    )