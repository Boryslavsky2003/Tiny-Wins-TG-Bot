import requests

from bot.config import settings


API_TOKEN = settings.HUGGINGFACE_TOKEN
MODEL_TEXT_URL = settings.MODEL_TEXT_URL

HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}


def generate_text(prompt: str) -> str:
    payload = {"inputs": prompt}
    response = requests.post(MODEL_TEXT_URL, headers=HEADERS, json=payload)
    result = response.json()

    try:
        return result[0]["generated_text"]
    except (KeyError, IndexError, TypeError):
        return "⚠️ Error: Could not generate text."
