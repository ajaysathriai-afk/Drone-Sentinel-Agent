from app.vectorstore.chroma_db import collection
from app.services.vision_service import client

from app.agents.db_tools import (
    count_incidents,
    latest_incident,
    get_recent_incidents
)

from app.agents.tool_router import (
    select_tool
)


def investigate(query: str):

    tool = select_tool(query)

    if tool == "count":

        total = count_incidents()

        return (
            f"There are currently "
            f"{total} incidents "
            f"in the system."
        )

    if tool == "latest":

        incident = latest_incident()

        if not incident:
            return "No incidents found."

        return (
            f"Latest Incident\n\n"
            f"Time: {incident.timestamp}\n"
            f"Event: {incident.event}"
        )


    if tool == "recent":

        incidents = get_recent_incidents()

        response = (
            "Recent Incidents\n\n"
        )

        for incident in incidents:

            response += (
                f"{incident.timestamp}"
                f" | {incident.event}\n"
            )

        return response

    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    documents = results.get(
        "documents",
        [[]]
    )[0]

    if not documents:

        return (
            "No matching incidents found."
        )

    context = "\n".join(documents)

    response = client.chat.completions.create(

        model="gpt-4o",

        messages=[
            {
                "role": "system",
                "content":
                """
                You are an AI security investigator.

                Analyze retrieved incidents.

                Provide a professional investigation report.

                Format:

                Findings:
                ...

                Risk Assessment:
                ...

                Recommended Action:
                ...

                Use plain text only.
                Do not use markdown.
                Do not use ** symbols.
                Keep response under 150 words.  
                """
            },
            {
                "role": "user",
                "content":
                f"""
User Question:
{query}

Retrieved Incidents:
{context}

Create a professional investigation report.
"""
            }
        ]
    )

    return response.choices[0].message.content