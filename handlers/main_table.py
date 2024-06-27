from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.filters import StateFilter
from aiogram.types import InputMediaPhoto, Message, CallbackQuery

from database.sqlite import Database
from file_work.media_codesa import pdc
from keyboards.blinking import get_back
from keyboards.dormitories import choose_dorm
from keyboards.helpers import helpers_obr_level
from keyboards.main_table import starting, MainTableCallBack
from keyboards.utils import utils

router = Router()
db = Database()


@router.message(CommandStart())
async def greeting(message: Message):
    user_id = message.from_user.id
    if not message.from_user.last_name:
        nick = f'{message.from_user.first_name}'
    else:
        nick = f'{message.from_user.first_name}_{message.from_user.last_name}'
    if not db.user_exists(user_id):
        db.add_user(user_id, nick)
        await message.answer_photo(photo=str(pdc()["main"][0]), caption=str(pdc()["main"][1]), parse_mode='HTML',
                                   reply_markup=starting())
    else:
        await message.answer_photo(photo=str(pdc()["main"][0]), caption=str(pdc()["main"][1]), parse_mode='HTML',
                                   reply_markup=starting())


@router.callback_query(MainTableCallBack.filter(F.changing_pic == True))
async def my_callback_foo(callback: CallbackQuery, callback_data: MainTableCallBack):
    if callback_data.open_str == "choose_dorm":
        await callback.message.edit_media(InputMediaPhoto(media=str(pdc()[f'{callback_data.open_str}'][0]),
                                                          caption=str(pdc()[f"{callback_data.open_str}"][1]),
                                                          parse_mode='HTML'), reply_markup=choose_dorm())
    elif callback_data.open_str == "helpers_obr_level":
        await callback.message.edit_media(InputMediaPhoto(media=str(pdc()[f'{callback_data.open_str}'][0]),
                                                          caption=str(pdc()[f"{callback_data.open_str}"][1]),
                                                          parse_mode='HTML'), reply_markup=helpers_obr_level())
    elif callback_data.open_str == "student_utils":
        await callback.message.edit_media(InputMediaPhoto(media=str(pdc()[f'{callback_data.open_str}'][0]),
                                                          caption=str(pdc()[f"{callback_data.open_str}"][1]),
                                                          parse_mode='HTML'), reply_markup=utils())
    else:
        await callback.message.edit_media(InputMediaPhoto(media=str(pdc()[f"{callback_data.open_str}"][0]),
                                                          caption=str(pdc()[f"{callback_data.open_str}"][1]),
                                                          parse_mode='HTML'), reply_markup=get_back(True))


@router.callback_query(MainTableCallBack.filter(F.changing_pic == False))
async def my_callback_foo(callback: CallbackQuery, callback_data: MainTableCallBack):
    await callback.message.edit_media(InputMediaPhoto(media=str(pdc()[f'{callback_data.open_str}'][0]),
                                                      caption=str(pdc()[f"{callback_data.open_str}"][1]),
                                                      parse_mode='HTML'), reply_markup=get_back(False))


@router.message(StateFilter(None))
async def greeting(message: Message):
    await message.answer_photo(photo=str(pdc()["main"][0]), caption=str(pdc()["main"][1]), parse_mode='HTML',
                               reply_markup=starting())
