from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

channel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="UA 🇺🇦", callback_data="ua"),
            InlineKeyboardButton(text="US 🇺🇸", callback_data="us"),
        ]
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
