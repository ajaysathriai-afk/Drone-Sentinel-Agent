from datetime import datetime

from app.database import SessionLocal
from app.models import Incident
from app.vectorstore.chroma_db import collection

from app.services.vision_service import analyze_drone_image
from app.services.yolo_service import (
    detect_objects,
    aggregate_objects
)


def yolo_node(state):

    detections = detect_objects(
        state["image_path"]
    )

    counts = aggregate_objects(
        detections
    )

    labels = []

    for label, count in counts.items():

        labels.extend(
            [label] * count
        )

    state["objects"] = labels
    state["object_counts"] = counts

    print("\nYOLO COUNTS:")
    print(counts)
    print("\n")

    return state


def vision_node(state):

    result = analyze_drone_image(
        state["image_bytes"]
    )

    print("\nVISION RESULT:")
    print(result)
    print("\n")

    state["analysis"] = result

    state["threat_level"] = result.get(
        "threat_level",
        "LOW"
    )

    counts = state.get(
        "object_counts",
        {}
    )

    summary_parts = []

    for label, count in counts.items():

        summary_parts.append(
            f"{label} x {count}"
        )

    state["summary"] = (
        "Detected: "
        + ", ".join(summary_parts)
    )

    return state


def object_extraction_node(state):

    return state


def threat_assessment_node(state):

    counts = state.get(
        "object_counts",
        {}
    )

    people = counts.get("person", 0)

    trucks = counts.get("truck", 0)

    buses = counts.get("bus", 0)

    cars = counts.get("car", 0)

    if people >= 5:

        state["threat_level"] = "HIGH"

    elif trucks >= 3:

        state["threat_level"] = "HIGH"

    elif people >= 1 and trucks >= 1:

        state["threat_level"] = "HIGH"

    elif buses >= 2:

        state["threat_level"] = "MEDIUM"

    elif cars >= 10:

        state["threat_level"] = "MEDIUM"

    else:

        state["threat_level"] = "LOW"

    # Assign zone based on dominant detected object
    counts = state.get("object_counts", {})
    if counts.get("person", 0) >= 1:
        state["zone"] = "Perimeter"
    elif counts.get("truck", 0) >= 1:
        state["zone"] = "Loading Dock"
    elif counts.get("car", 0) >= 5:
        state["zone"] = "Parking"
    elif counts.get("bus", 0) >= 1:
        state["zone"] = "Entry Gate"
    else:
        state["zone"] = "General"

    return state

def alert_generation_node(state):

    counts = state.get(
        "object_counts",
        {}
    )

    people = counts.get("person", 0)

    cars = counts.get("car", 0)

    trucks = counts.get("truck", 0)

    if people >= 5:

        state["alert_message"] = (
            "Crowd activity detected in monitored area."
        )

    elif people >= 1 and trucks >= 1:

        state["alert_message"] = (
            "Person detected near heavy vehicles."
        )

    elif trucks >= 3:

        state["alert_message"] = (
            "Multiple trucks detected in monitored zone."
        )

    elif cars >= 10:

        state["alert_message"] = (
            "High vehicle concentration detected."
        )

    else:

        state["alert_message"] = (
            "Normal activity observed."
        )

    state["summary"] = state["alert_message"]

    return state


def storage_node(state):

   
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
    db.commit()
    db.refresh(incident)
    db.close()

    document = f"""
    Image: {state.get("image_name")}

    Timestamp: {incident.timestamp}

    Zone: {state.get("zone")}

    Threat Level: {state.get("threat_level")}

    Detected Objects:
    {", ".join(state["objects"])}

    Alert:
    {state["alert_message"]}

    Vision Summary:
    {state["analysis"]["short_summary"]}
    """

    print("METADATA:", {
        "zone": state.get("zone"),
        "threat": state.get("threat_level"),
        "image": state.get("image_name"),
    })


    collection.add(
        ids=[str(incident.id)],
        documents=[document],
        metadatas=[
            {
                "zone": str(state.get("zone") or "General"),
                "threat": str(state.get("threat_level") or "LOW"),
                "image": str(state.get("image_name") or "unknown.jpg"),
            }
        ]
    )