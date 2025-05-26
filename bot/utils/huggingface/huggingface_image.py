import requests
from loguru import logger

from bot.config import settings

API_TOKEN = settings.HUGGINGFACE_TOKEN
MODEL_IMAGE_URL = settings.MODEL_IMAGE_URL

HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}


def generate_image(prompt: str, filename="generated_image.png") -> str:
    logger.debug(f"[HF] 📤 Надсилаємо prompt: '{prompt}' → {MODEL_IMAGE_URL}")

    response = requests.post(MODEL_IMAGE_URL, headers=HEADERS, json={"inputs": prompt})

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        logger.debug(f"[HF] ✅ Зображення збережено → {filename}")
        return filename
    else:
        logger.error(f"[HF] ❌ Помилка API {response.status_code}: {response.text}")
        raise RuntimeError(f"HuggingFace API error {response.status_code}")
