from pathlib import Path

from app.agents.workflow import graph

IMAGES_DIR = Path(
    "data/images"
)

images = sorted(
    IMAGES_DIR.glob("*")
)

for image_path in images:

    print(
        f"Processing {image_path.name}"
    )

    with open(
        image_path,
        "rb"
    ) as f:

        image_bytes = f.read()

    state = {
        "image_bytes": image_bytes
    }

    graph.invoke(state)

print(
    f"\nProcessed {len(images)} images"
)
