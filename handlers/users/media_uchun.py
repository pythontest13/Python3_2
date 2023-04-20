from aiogram import types

from loader import dp,bot
from aiogram.types import ContentType, InputFile
from filters.shaxsiy_uchun import Shaxsiy

# Echo bot


@dp.message_handler(Shaxsiy(),text="Sho'rva")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_link = 'https://t.me/uzpythonjobs/601'
    await bot.send_photo(chat_id=user_id,photo=rasm_link,caption="Narxi --- 20 ming")
