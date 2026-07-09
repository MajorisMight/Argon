class ContextBuilder:

    def build(self, question, context):

        return f"""
User Question:
{question}

Retrieved Context:
{context}

Using ONLY the retrieved context, answer the user's question naturally.
"""