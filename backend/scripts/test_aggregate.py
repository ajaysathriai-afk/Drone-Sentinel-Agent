from app.services.yolo_service import (
    detect_objects,
    aggregate_objects
)

detections = detect_objects(
    "data/images/image_001.jpg"
)

counts = aggregate_objects(
    detections
)

print(counts)
