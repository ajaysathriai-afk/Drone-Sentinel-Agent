from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import tempfile

from app.agents.workflow import graph

router = APIRouter()


@router.post("/")
async def analyze_image(
    file: UploadFile = File(...)
):

    image_bytes = await file.read()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as temp:

        temp.write(
            image_bytes
        )

        image_path = temp.name

    result = graph.invoke(
        {
            "image_bytes": image_bytes,
            "image_path": image_path
        }
    )

    result.pop(
        "image_bytes",
        None
    )

    return result