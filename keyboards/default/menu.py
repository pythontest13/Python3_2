from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_bottons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Taomlar"),
            KeyboardButton(text="Ichimliklar")
        ],
        [
            KeyboardButton(text="Shirinliklar"),
            KeyboardButton(text="Fast food"),
            KeyboardButton(text="Milliy taomlar")
        ],
        [
            KeyboardButton(text="Adminga murojat")
        ]

    ],
    resize_keyboard=True
)

menu_bottons_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dishes"),
            KeyboardButton(text="Dirinks")
        ],
        [
            KeyboardButton(text="Deserts"),
            KeyboardButton(text="Fast food")
        ]

    ],
    resize_keyboard=True
)


tasdiqlash_bottons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Xa"),
            KeyboardButton(text="Yo'q")
        ],


    ],
    resize_keyboard=True
)
