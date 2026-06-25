import base64
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_drone_image(
    image_bytes: bytes
):
    image_base64 = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4o",

        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text":
                        """
                        Analyze this drone security image.

                        Return ONLY valid JSON.

                        Format:

                        {
                           "objects_detected": [],
                           "threat_level": "",
                           "short_summary": ""
                        }

                        Threat Levels:

                        LOW
                        MEDIUM
                        HIGH
                        CRITICAL

                        Example:

                        {
                            "objects_detected": ["person"],
                            "threat_level": "MEDIUM",
                            "short_summary": "Person detected near perimeter fence."
                        }
                        """
                    },

                    {
                        "type": "image_url",
                        "image_url": {
                            "url":
                            f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    )

    content = response.choices[0].message.content

    content = (
        content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        return json.loads(content)

    except Exception as e:

        print("JSON ERROR:", e)
        print("CONTENT:", content)

        return {
            "objects_detected": [],
            "threat_level": "LOW",
            "short_summary": "Unable to parse model response."
        } 