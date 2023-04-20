from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

taomlar_bottons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sho'rva"),
            KeyboardButton(text="Osh"),
            KeyboardButton(text="Baliq")
        ],
        [
            KeyboardButton(text="Shashlik"),
            KeyboardButton(text="Somsa")
        ]
    ],
    resize_keyboard=True
)























taomlar_bottons_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Soup"),
            KeyboardButton(text="Pilaf"),
            KeyboardButton(text="Fish")
        ],
        [
            KeyboardButton(text="Shashlik"),
            KeyboardButton(text="Somsa")
        ]
    ],
    resize_keyboard=True
)