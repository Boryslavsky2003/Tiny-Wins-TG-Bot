# bot/utils/ai_checker.py

import requests
from typing import Optional, Tuple
from pathlib import Path
from bot.config import settings


class AIChecker:
    """
    Клас для перевірки роботоспособності AI моделей через Hugging Face API.
    Використовує налаштування з bot.config.settings.
    """

    def __init__(self):
        self.headers = {"Authorization": f"Bearer {settings.HUGGINGFACE_TOKEN}"}
        self.text_model_url = settings.MODEL_TEXT_URL
        self.image_model_url = settings.MODEL_IMAGE_URL
        self.timeout = 30  # секунд очікування відповіді

    def check_text_model(
        self, prompt: str = "Напиши коротку мотиваційну цитату"
    ) -> Tuple[bool, str]:
        """
        Перевіряє роботу текстової моделі.
        Повертає (success, result), де success - bool, result - текст або помилка.
        """
        try:
            response = requests.post(
                self.text_model_url,
                headers=self.headers,
                json={"inputs": prompt, "wait_for_model": True},
                timeout=self.timeout,
            )

            if response.status_code == 200:
                return True, response.json()[0]["generated_text"]
            return False, f"Text model error {response.status_code}: {response.text}"

        except Exception as e:
            return False, f"Text model exception: {str(e)}"

    def check_image_model(
        self,
        prompt: str = "Кіт у космосі, цифровий арт",
        save_path: Optional[str] = None,
    ) -> Tuple[bool, str]:
        """
        Перевіряє роботу моделі генерації зображень.
        Повертає (success, result), де success - bool, result - шлях до файлу або помилка.
        """
        try:
            if save_path is None:
                save_path = Path("temp_ai_check_image.png").absolute()

            response = requests.post(
                self.image_model_url,
                headers=self.headers,
                json={"inputs": prompt, "wait_for_model": True},
                timeout=self.timeout,
            )

            if response.status_code == 200:
                with open(save_path, "wb") as f:
                    f.write(response.content)
                return True, str(save_path)
            return False, f"Image model error {response.status_code}: {response.text}"

        except Exception as e:
            return False, f"Image model exception: {str(e)}"

    def run_full_check(self) -> dict:
        """
        Виконує повну перевірку обох моделей.
        Повертає словник з результатами.
        """
        results = {
            "text_model": {"url": self.text_model_url, "status": "pending"},
            "image_model": {"url": self.image_model_url, "status": "pending"},
        }

        # Перевірка текстової моделі
        text_success, text_result = self.check_text_model()
        results["text_model"]["status"] = "working" if text_success else "failed"
        results["text_model"]["result"] = text_result

        # Перевірка моделі зображень
        img_success, img_result = self.check_image_model()
        results["image_model"]["status"] = "working" if img_success else "failed"
        results["image_model"]["result"] = img_result

        return results


if __name__ == "__main__":
    # Приклад використання
    checker = AIChecker()

    print("🔍 Running AI models health check...")
    results = checker.run_full_check()

    print("\n📝 Text model results:")
    print(f"Status: {results['text_model']['status']}")
    print(f"URL: {results['text_model']['url']}")
    print(f"Test output: {results['text_model']['result'][:200]}...")

    print("\n🖼️ Image model results:")
    print(f"Status: {results['image_model']['status']}")
    print(f"URL: {results['image_model']['url']}")
    print(f"Image saved to: {results['image_model']['result']}")
