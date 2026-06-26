from pathlib import Path

from app.agents.workflow import graph

IMAGE_DIR = Path("data/images")

images = sorted(IMAGE_DIR.glob("*.jpg"))

print(f"\nFound {len(images)} images.\n")

for i, image_path in enumerate(images, start=1):

    print(f"[{i}/{len(images)}] Processing {image_path.name}")

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    result = graph.invoke(
        {
            "image_path": str(image_path),
            "image_bytes": image_bytes,
            "image_name": image_path.name,
        }
    )

    print(
        f"✓ {result.get('threat_level', 'UNKNOWN')} "
        f"- {result.get('alert_message', '')}"
    )

print("\nDone!")
