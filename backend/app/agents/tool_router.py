def select_tool(query: str):

    query = query.lower()

    if (
        "count" in query
        or "how many" in query
    ):
        return "count"

    if (
        "latest" in query
        or "last incident" in query
    ):
        return "latest"

    if "recent" in query:
        return "recent"

    return "semantic"