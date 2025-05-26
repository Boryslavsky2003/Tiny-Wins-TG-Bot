from loguru import logger
from bot.utils.huggingface import huggingface_image


def generate_image_with_prompt(prompt: str, output_path: str) -> str:
    try:
        return huggingface_image.generate_image(prompt, output_path)
    except Exception as e:
        logger.error(f"Image generation failed: {str(e)}")
        raise
