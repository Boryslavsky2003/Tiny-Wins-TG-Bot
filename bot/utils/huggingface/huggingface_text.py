import requests
from loguru import logger

from bot.config import settings


API_TOKEN = settings.HUGGINGFACE_TOKEN
MODEL_TEXT_URL = settings.MODEL_TEXT_URL
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}


def generate_text(prompt: str) -> str:
    payload = {"inputs": prompt}

    try:
        response = requests.post(
            MODEL_TEXT_URL, headers=HEADERS, json=payload, timeout=30
        )

        if response.status_code == 402:
            logger.error(
                "[HF] ❌ API error 402: Payment Required — exceeded free tier credits."
            )
            return "⚠️ Вичерпано ліміт генерації. Оновіть підписку Hugging Face або спробуйте пізніше."

        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]

        logger.warning(f"[HF] ⚠️ Unexpected response format: {result}")
        return "⚠️ Сталася помилка під час генерації тексту."

    except requests.exceptions.RequestException as e:
        logger.error(f"[HF] ❌ Запит не вдався: {str(e)}")
        return "⚠️ Не вдалося з'єднатися з Hugging Face API."

    except Exception as e:
        logger.error(f"[HF] ❌ Невідома помилка: {str(e)}")
        return "⚠️ Невідома помилка під час генерації тексту."
