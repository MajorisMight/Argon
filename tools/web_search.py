from ddgs import DDGS


def web_search(query, max_results=5):
    """
    Searches the web via DuckDuckGo (no API key needed) and returns a
    short list of results: title, URL, and snippet for each.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
    except Exception as e:
        return f"Search failed: {e}"

    if not results:
        return "No results found."

    formatted = []
    for i, r in enumerate(results, 1):
        title = r.get("title", "")
        href = r.get("href", "")
        body = r.get("body", "")
        formatted.append(f"{i}. {title}\n   {href}\n   {body}")

    return "\n\n".join(formatted)


web_search_tool = {
    "name": "web_search",
    "description": (
        "Searches the web for current information and returns a list of "
        "results with title, URL, and snippet. Use this for questions "
        "about current events, recent facts, or anything that might be "
        "outside your training data."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "The search query"},
            "max_results": {
                "type": "integer",
                "description": "Number of results to return (default 5)",
            },
        },
        "required": ["query"],
    },
}
