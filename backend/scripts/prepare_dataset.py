import random
import shutil
from pathlib import Path

OUTPUT_DIR = Path("data/images")

VISDRONE_DIR = Path(
    "data/datasets/visdrone"
)

HUMAN_DIR = Path(
    "data/datasets/human_detection/human detection dataset"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

visdrone_images = list(
    VISDRONE_DIR.rglob("*.jpg")
)

human_images = list(
    HUMAN_DIR.rglob("*.png")
)

selected_visdrone = random.sample(
    visdrone_images,
    25
)

selected_human = random.sample(
    human_images,
    25
)

counter = 1

for image in (
    selected_visdrone +
    selected_human
):

    destination = (
        OUTPUT_DIR /
        f"image_{counter:03d}{image.suffix}"
    )

    shutil.copy(
        image,
        destination
    )

    counter += 1

print(
    f"Copied {counter - 1} images"
)
