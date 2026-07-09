from tools.vector_store import load_vector_store


def retrieve_document(query, k=3):

    db = load_vector_store()
    docs = db.similarity_search(query, k=k)

    context = ""

    for i, doc in enumerate(docs, 1):
        context += (
            f"Chunk {i}\n"
            f"Metadata: {doc.metadata}\n"
            f"Content:\n{doc.page_content}\n\n"
        )

    return context

retrieve_document_tool = {
    "name": "retrieve_document",
    "description": "Retrieve relevant information from indexed documents to answer user questions.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The user's question."
            }
        },
        "required": ["query"]
    }
}