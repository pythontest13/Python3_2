from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from filters.shaxsiy_uchun import Shaxsiy
from states.holatlar import Form
from  keyboards.default.menu import tasdiqlash_bottons,menu_bottons
# Echo bot
@dp.message_handler(Shaxsiy(),text="Adminga murojat")
async def bot_echo(message: types.Message):

    await message.answer(text="Ismizi kiriting")
    await Form.ism_holati.set()


@dp.message_handler(Shaxsiy(), state=Form.ism_holati)
async def bot_echo(message: types.Message, state : FSMContext):
    ism = message.text
    await state.update_data({'ismi' : ism})
    await message.answer(text="Familyani kiriting")
    await Form.fam_holati.set()


@dp.message_handler(Shaxsiy(), state=Form.fam_holati)
async def bot_echo(message: types.Message, state : FSMContext):
    familya = message.text
    await state.update_data({'fam' : familya})
    await message.answer(text="Telni kiriting")
    await Form.tel_holati.set()

@dp.message_handler(Shaxsiy(), state=Form.tel_holati)
async def bot_echo(message: types.Message, state : FSMContext):
    tel = message.text
    await state.update_data({'telefon' : tel})
    await message.answer(text="Manzilni kiriting")
    await Form.manzil_holati.set()


@dp.message_handler(Shaxsiy(), state=Form.manzil_holati)
async def bot_echo(message: types.Message, state : FSMContext):
    address = message.text
    await state.update_data({'manzil' : address})

    await message.answer(text="Takliflarizi kiriting")
    await Form.murojaat_holati.set()


@dp.message_handler(Shaxsiy(), state=Form.murojaat_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    murajjat = message.text
    await state.update_data({'taklif': murajjat})

    malumot = await state.get_data()
    ism = malumot.get('ismi')
    fam = malumot.get('fam')
    telfon = malumot.get('telefon')
    manzil = malumot.get('manzil')
    text = malumot.get('taklif')

    user_id = message.from_user.id
    umumiy_malumot = f"Ismi : {ism}\n" \
                     f"Familya : {fam}\n" \
                     f"Telefon : {telfon}\n" \
                     f"Manzil : {manzil}\n" \
                     f"Taklif : {text}\n"

    await bot.send_message(chat_id=user_id, text=umumiy_malumot)
    await bot.send_message(chat_id=user_id,text="Hamma ma'lumotlar to'g'rimi ?", reply_markup=tasdiqlash_bottons)
    await Form.tasqidlash_holati.set()


@dp.message_handler(Shaxsiy(), state=Form.tasqidlash_holati,text="Xa")
async def bot_echo(message: types.Message, state : FSMContext):
    address = message.text

    malumot = await state.get_data()
    ism = malumot.get('ismi')
    fam = malumot.get('fam')
    telfon = malumot.get('telefon')
    manzil = malumot.get('manzil')
    text = malumot.get('taklif')
    username = message.from_user.username
    user_id = message.from_user.id
    umumiy_malumot = f"👤Ismi : {ism}\n" \
                     f"Familya : {fam}\n" \
                     f"📱Telefon : {telfon}\n" \
                     f"Manzil : {manzil}\n" \
                     f"Taklif : {text}\n" \
                     f"Username : @{username}\n"

    await message.answer(text="Adminga yuborildi")
    await bot.send_message(chat_id='789362160',text=umumiy_malumot,reply_markup=menu_bottons)
    await state.finish()

@dp.message_handler(Shaxsiy(), state=Form.tasqidlash_holati, text="Yo'q")
async def bot_echo(message: types.Message, state : FSMContext):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,  text="Bekor qilindi",reply_markup=menu_bottons)
    await state.finish()
