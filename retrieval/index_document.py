from tools.document_understanding import doc_reader
from retrieval.cleaner import clean_markdown
from retrieval.chunking import create_documents
from retrieval.vector_store import create_vector_store


def index_document(path):

    markdown = doc_reader(path)

    markdown = clean_markdown(markdown)

    documents = create_documents(markdown)

    create_vector_store(documents)

    return f"Indexed {len(documents)} chunks successfully."


index_document_tool = {
    "name": "index_document",
    "description": "Convert a PDF into markdown and prepare it for retrieval.",
    "parameters": {
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "Path to the PDF file"
            }
        },
        "required": ["path"]
    }
}