import os

from aiogram import Router, F, html, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, InputMediaPhoto
from dotenv import load_dotenv

from database.sqlite import Database
from file_work.media_codesa import pdc
from keyboards.admin import AdminCallBack, announce_approve, admin_panel
from keyboards.blinking import announce

db = Database()
router = Router()


class Announce(StatesGroup):
    text = State()


async def make_announce(text, users=db.all_users()):
    load_dotenv()
    bot = Bot(os.getenv('TOKEN'))
    for user in users:
        await bot.send_message(chat_id=str(user), text=f'{text}')


@router.callback_query(AdminCallBack.filter(F.action == "announce"))
async def my_callback_foo(callback: CallbackQuery, callback_data: AdminCallBack, state: FSMContext):
    await state.clear()
    await callback.message.edit_media(InputMediaPhoto(media=str(pdc()[f"{callback_data.action}"][0]),
                                                      caption=str(pdc()[f"{callback_data.action}"][1]),
                                                      parse_mode='HTML'), reply_markup=announce())
    await state.set_state(Announce.text)


@router.message(Announce.text)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    if message.text in ["/start", '/admin']:
        await message.reply(
            'Чтобы вернуться в главное меню или меню администратора, сначала выйдите из режима создания объявления!')
    else:
        await state.update_data(text=f'{html.quote(message.text)}')
        await message.answer_photo(photo=str(pdc()["announce_approval"][0]),
                                   caption=f'{str(pdc()["announce_approval"][1])}\n' + f'{html.quote(message.text)}',
                                   parse_mode='HTML', reply_markup=announce_approve())


@router.callback_query(AdminCallBack.filter(F.action == "announce_approval"))
async def my_callback_foo(callback: CallbackQuery, callback_data: AdminCallBack, state: FSMContext):
    await callback.message.answer_photo(photo=str(pdc()[f"{callback_data.action}"][0]),
                                        caption=str(pdc()[f"{callback_data.action}"][1]), parse_mode='HTML',
                                        reply_markup=admin_panel())
    await callback.message.delete()
    announcement = await state.get_data()
    await make_announce(text=announcement["text"])
    await state.clear()
