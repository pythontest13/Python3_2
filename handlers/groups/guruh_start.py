from aiogram import types

from filters import Guruh
from loader import dp,bot
from aiogram.types import ContentType

# Echo bot
@dp.message_handler(commands='start')
async def bot_echo(message: types.Message):
    await message.answer(text="Guruhga hush kelibsiz! ")


@dp.message_handler(text='salom')
async def bot_echo(message: types.Message):
    await message.reply(text="Assalomu allaykum ")


@dp.message_handler(content_types=ContentType.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    ism = message.new_chat_members[0].first_name
    guruh_id = message.chat.id
    msg = message.message_id
    await message.reply(text=f"Salom botga hush kelibsiz {ism} ")
    await bot.delete_message(chat_id=guruh_id,message_id=msg)

@dp.message_handler(content_types=ContentType.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    ism = message.left_chat_member.first_name
    guruh_id = message.chat.id
    msg = message.message_id
    await message.reply(text=f"Guruhni tark edti  {ism} !")
    await bot.delete_message(chat_id=guruh_id,message_id=msg)


@dp.message_handler(text='ilon')
async def bot_echo(message: types.Message):
    guruh_id = message.chat.id
    user_id = message.from_user.id

    await bot.restrict_chat_member(chat_id=guruh_id,user_id=user_id,until_date='1')