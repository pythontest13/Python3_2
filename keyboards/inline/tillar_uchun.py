from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tillar_bottons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili🇺🇿", callback_data="til1"),
            InlineKeyboardButton(text="Inglis tili🇬🇧",callback_data="til2")
        ],
        [
            InlineKeyboardButton(text="Hamkorlarimiz",url='https://t.me/campyuteruchun'),
            InlineKeyboardButton(text="Ulashish",switch_inline_query='Shu botga a\'zo bo\'ling')
        ]
    ]
)

print("Salom dasturchi")

soz = "Salom dasturchi"
print(soz)