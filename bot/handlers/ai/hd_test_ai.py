from aiogram.filters import Command
from aiogram import Router

from bot.utils.huggingface.test_huggingface import AIChecker


router = Router()


@router.message(Command("test_ai"))
def test_ai():
    checker = AIChecker()
    results = checker.run_full_check()

    if results["text_model"]["status"] == "working":
        print("✅ Текстова модель працює нормально")
    else:
        print(f"❌ Проблема з текстовою моделлю: {results['text_model']['result']}")

    if results["image_model"]["status"] == "working":
        print("✅ Модель зображень працює нормально")
    else:
        print(f"❌ Проблема з моделлю зображень: {results['image_model']['result']}")
