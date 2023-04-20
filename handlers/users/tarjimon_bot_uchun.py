from aiogram import types
from googletrans import Translator
from loader import dp

tarjima = Translator()
# Echo bot
@dp.message_handler()
async def bot_echo(message: types.Message):
    til = tarjima.detect(text=message.text).lang
    if til == 'uz':
        tarjima_qil_en = tarjima.translate(text=message.text,dest='en',src='uz').text
        await message.answer(tarjima_qil_en)

    elif til == 'en':
        tarjima_qil_en = tarjima.translate(text=message.text,dest='ru',src='en').text
        await message.answer(tarjima_qil_en)
