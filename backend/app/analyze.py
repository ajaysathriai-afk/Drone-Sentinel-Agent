from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.services.vision_service import (
    analyze_drone_image
)

router = APIRouter()


@router.post("/")
async def analyze_image(
    file: UploadFile = File(...)
):
    image_bytes = await file.read()

    result = analyze_drone_image(
        image_bytes
    )

    return {
        "filename": file.filename,
        "analysis": result
    }
