from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.utils.callback_data import BotCallback

from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)


def create_admin_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text="📝 Згенерувати текст",
        callback_data=BotCallback(action="create_text_ai").pack(),
    )
    builder.button(
        text="🎨 Згенерувати зображення",
        callback_data=BotCallback(action="create_image_ai").pack(),
    )
    builder.button(
        text="Інші команди",
        callback_data=BotCallback(action="other_commands").pack(),
    )

    builder.adjust(2, 1)
    return builder.as_markup()


def create_other_commands_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🤖 Протестувати AI-моделі",
                    callback_data=BotCallback(action="test_ai").pack(),
                ),
                InlineKeyboardButton(
                    text="🆔 Отримати ID",
                    callback_data=BotCallback(action="get_id").pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Повернутись",
                    callback_data=BotCallback(action="go_back").pack(),
                )
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
