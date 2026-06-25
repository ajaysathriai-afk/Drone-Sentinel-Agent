from langgraph.graph import StateGraph

from app.agents.state import DroneState

from app.agents.nodes import (
    yolo_node,
    vision_node,
    object_extraction_node,
    threat_assessment_node,
    alert_generation_node,
    storage_node
)

builder = StateGraph(
    DroneState
)

builder.add_node(
    "yolo",
    yolo_node
)


builder.add_node(
    "vision",
    vision_node
)

builder.add_node(
    "objects",
    object_extraction_node
)

builder.add_node(
    "threat",
    threat_assessment_node
)

builder.add_node(
    "alert",
    alert_generation_node
)

builder.set_entry_point(
    "yolo"
)


builder.add_edge(
    "yolo",
    "vision"
)

builder.add_edge(
    "vision",
    "objects"
)


builder.add_edge(
    "objects",
    "threat"
)

builder.add_edge(
    "threat",
    "alert"
)

builder.set_finish_point(
    "alert"
)

builder.add_node(
    "storage",
    storage_node
)

builder.add_edge(
    "alert",
    "storage"
)

builder.set_finish_point(
    "storage"
)

graph = builder.compile()
