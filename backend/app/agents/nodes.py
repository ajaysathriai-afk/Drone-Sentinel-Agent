def storage_node(state):

    from app.models import Alert

    db = SessionLocal()

    incident = Incident(
        image_name=state.get("image_name", "unknown.jpg"),
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M"),
        event=state["alert_message"],
        detected_objects=",".join(state.get("objects", [])),
        zone=state.get("zone", "General"),
        threat_level=state.get("threat_level", "LOW")
    )

    db.add(incident)

    # Create alert only for HIGH / CRITICAL threats
    if state.get("threat_level") in ["HIGH", "CRITICAL"]:

        alert = Alert(
            severity=state["threat_level"],
            message=state["alert_message"]
        )

        db.add(alert)

    db.commit()
    db.refresh(incident)

    document = f"""
Image: {state.get("image_name")}

Timestamp: {incident.timestamp}

Zone: {state.get("zone")}

Threat Level: {state.get("threat_level")}

Detected Objects:
{", ".join(state.get("objects", []))}

Alert:
{state["alert_message"]}

Vision Summary:
{state["analysis"]["short_summary"]}
"""

    print(
        "METADATA:",
        {
            "zone": state.get("zone"),
            "threat": state.get("threat_level"),
            "image": state.get("image_name"),
        },
    )

    collection.add(
        ids=[str(incident.id)],
        documents=[document],
        metadatas=[
            {
                "zone": str(state.get("zone") or "General"),
                "threat": str(state.get("threat_level") or "LOW"),
                "image": str(state.get("image_name") or "unknown.jpg"),
            }
        ],
    )

    db.close()

    return state