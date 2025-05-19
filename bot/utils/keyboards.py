from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)


def create_admin_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📝 Згенерувати текст",
                    callback_data="create_text_ai",
                ),
                InlineKeyboardButton(
                    text="🎨 Згенерувати зображення",
                    callback_data="create_image_ai",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🤖 Протестувати AI-моделі",
                    callback_data="test_ai",
                ),
                InlineKeyboardButton(
                    text="🆔 Отримати ID",
                    callback_data="get_id",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❗ Допомога з ботом",
                    callback_data="help_bot",
                ),
            ],
        ]
    )


def create_test_keyboard() -> ReplyKeyboardMarkup:
    faq_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Що робити, якщо у мене виникла помилка?")],
            [KeyboardButton(text="⬅️ Повернутися до головного меню")],
        ],
        resize_keyboard=True,
    )
    return faq_keyboard
