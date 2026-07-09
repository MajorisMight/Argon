from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_core.documents import Document

headers_to_split_on = [
    ("#", "H1"),
    ("##", "H2"),
    ("###", "H3"),
]

def create_documents(markdown: str):

    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on
    )

    chunks = splitter.split_text(markdown)

    documents = []

    for chunk in chunks:
        documents.append(
            Document(
                page_content=chunk.page_content,
                metadata=chunk.metadata
            )
        )

    return documents