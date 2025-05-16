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
                    text="📝 Створити текст за допомогою ШІ",
                    callback_data="create_text_ai",
                ),
                InlineKeyboardButton(
                    text="🎨 Згенерувати зображення на основі текстового опису",
                    callback_data="create_image_ai",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🤖 Протестувати AI-моделі", callback_data="test_ai"
                ),
                InlineKeyboardButton(
                    text="🆔 Отримати свій ID або ID каналу", callback_data="get_id"
                ),
            ],
        ]
    )


def create_test_keyboard() -> ReplyKeyboardMarkup:
    faq_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Які документи потрібно надсилати?"),
                KeyboardButton(text="Чи можна надсилати документи з 'Дії'?"),
            ],
            [
                KeyboardButton(
                    text="Що робити, якщо я не маю диплома/військового документа?"
                ),
                KeyboardButton(text="Які вимоги до якості фото документів?"),
            ],
            [
                KeyboardButton(text="Що робити, якщо бот каже, що фото нечітке?"),
                KeyboardButton(text="Скільки часу займе обробка документів?"),
            ],
            [
                KeyboardButton(text="Куди зберігаються мої документи?"),
                KeyboardButton(text="Чи безпечно передавати мої документи через бота?"),
            ],
            [KeyboardButton(text="Що робити, якщо у мене виникла помилка?")],
            [KeyboardButton(text="⬅️ Повернутися до головного меню")],
        ],
        resize_keyboard=True,
    )
    return faq_keyboard
