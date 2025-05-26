from loguru import logger
import aiofiles

from bot.utils.huggingface import huggingface_text, huggingface_image


async def complex_test_ai_model():
    logger.info("Testing AI models...")
    test_text = await test_text_model()
    test_image = await test_image_model()

    logger.info(f"Text model test result: {test_text[:100]}...")
    logger.info(f"Image model test saved to: {test_image}")


async def test_text_model() -> str:
    """Тестирование текстовой модели"""
    try:
        response = huggingface_text.generate_text(
            "Напиши коротку мотиваційну цитату українською, про 'Сонячний ранок у лісі, акварельний стиль'"
        )
        async with aiofiles.open(
            "ai/ai_test_gen/test_generated_text.txt", mode="w", encoding="utf-8"
        ) as f:
            await f.write(response)
        return response
    except Exception as e:
        logger.error(f"Text model test failed: {str(e)}")
        return f"Error: {str(e)}"


async def test_image_model() -> str:
    """Тестирование модели изображений"""
    try:
        return huggingface_image.generate_image(
            "Сонячний ранок у лісі, акварельний стиль",
            "ai/ai_test_gen/test_generated_image.png",
        )
    except Exception as e:
        logger.error(f"Image model test failed: {str(e)}")
        return f"Error: {str(e)}"
