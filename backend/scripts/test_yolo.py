from app.services.yolo_service import (
    detect_objects
)

results = detect_objects(
    "data/images/image_001.jpg"
)

print(results)
