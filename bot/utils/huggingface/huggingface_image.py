import requests

from bot.config import settings


API_TOKEN = settings.HUGGINGFACE_TOKEN
MODEL_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}


def generate_image(prompt: str, filename="generated_image.png") -> str:
    response = requests.post(MODEL_URL, headers=HEADERS, json={"inputs": prompt})

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        return filename
    else:
        return None
