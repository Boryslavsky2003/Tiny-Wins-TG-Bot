import requests

from bot.config import settings


API_TOKEN = settings.HUGGINGFACE_TOKEN
MODEL_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}


def generate_text(prompt: str) -> str:
    payload = {"inputs": prompt}
    response = requests.post(MODEL_URL, headers=HEADERS, json=payload)
    result = response.json()

    try:
        return result[0]["generated_text"]
    except (KeyError, IndexError, TypeError):
        return "⚠️ Error: Could not generate text."
