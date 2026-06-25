from ultralytics import YOLO

model = YOLO("yolov8n.pt")


def detect_objects(image_path):

    results = model(image_path)

    detections = []

    for result in results:

        for box in result.boxes:

            class_id = int(
                box.cls[0]
            )

            confidence = float(
                box.conf[0]
            )

            label = result.names[
                class_id
            ]

            detections.append(
                {
                    "label": label,
                    "confidence":
                    round(
                        confidence,
                        2
                    )
                }
            )

    return detections

from collections import Counter


def aggregate_objects(
    detections
):

    labels = [
        item["label"]
        for item in detections
    ]

    return dict(
        Counter(labels)
    )