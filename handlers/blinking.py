from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import InputMediaPhoto, CallbackQuery

from file_work.media_codesa import pdc
from keyboards.admin import admin_panel
from keyboards.blinking import BackingCallBack
from keyboards.dormitories import choose_dorm, after_choosing_dorm, DormCallBack
from keyboards.helpers import helpers_obr_level
from keyboards.main_table import starting
from keyboards.utils import utils

router = Router()


@router.callback_query(BackingCallBack.filter(F.open_str == "choose_dorm"))
async def my_callback_foo(callback: CallbackQuery, callback_data: BackingCallBack):
    if callback_data.from_file == False:
        await callback.message.edit_media(InputMediaPhoto(media=str(pdc()[f"{callback_data.open_str}"][0]),
                                                          caption=str(pdc()[f"{callback_data.open_str}"][1]),
                                                          parse_mode='HTML'), reply_markup=choose_dorm())
    else:
        await callback.message.answer_photo(photo=str(pdc()[f"{callback_data.open_str}"][0]),
                                            caption=str(pdc()[f"{callback_data.open_str}"][1]), parse_mode='HTML',
                                            reply_markup=choose_dorm())
        await callback.message.delete()


@router.callback_query(DormCallBack.filter(F.open_str.startswith("dorm_")))
async def my_callback_foo(callback: CallbackQuery, callback_data: BackingCallBack):
    await callback.message.answer_photo(str(pdc()[f"{callback_data.open_str}"][0]),
                                        caption=str(pdc()[f"{callback_data.open_str}"][1]), parse_mode='HTML',
                                        reply_markup=after_choosing_dorm(callback_data.dorm))
    await callback.message.delete()


@router.callback_query(BackingCallBack.filter(F.open_str == "main"))
async def my_callback_foo(callback: CallbackQuery, callback_data: BackingCallBack, state: FSMContext):
    try:
        await state.clear()
    except Exception:
        pass
    if callback_data.changing_pic:
        await callback.message.edit_media(InputMediaPhoto(media=str(pdc()[f"{callback_data.open_str}"][0]),
                                                          caption=str(pdc()[f"{callback_data.open_str}"][1]),
                                                          parse_mode='HTML'), reply_markup=starting())
    else:
        await callback.message.edit_caption(caption=str(pdc()[f"{callback_data.open_str}"][1]), parse_mode='HTML',
                                            reply_markup=starting())


@router.callback_query(BackingCallBack.filter(F.open_str == "admin_panel"))
async def my_callback_foo(callback: CallbackQuery, callback_data: BackingCallBack, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await callback.message.edit_caption(caption=str(pdc()[f"{callback_data.open_str}"][1]), parse_mode='HTML',
                                        reply_markup=admin_panel())


@router.callback_query(BackingCallBack.filter(F.open_str == "helpers_obr_level"))
async def my_callback_foo(callback: CallbackQuery, callback_data: BackingCallBack, state: FSMContext):
    await state.clear()
    await callback.message.edit_caption(caption=str(pdc()[f"{callback_data.open_str}"][1]), parse_mode='HTML',
                                        reply_markup=helpers_obr_level())


@router.callback_query(BackingCallBack.filter(F.open_str == "from_helpers_to_main"))
async def my_callback_foo(callback: CallbackQuery, callback_data: BackingCallBack, state: FSMContext):
    await state.clear()
    await callback.message.answer_photo(photo=str(pdc()["main"][0]), caption=str(pdc()["main"][1]), parse_mode='HTML',
                                        reply_markup=starting())
    await callback.message.delete()


@router.callback_query(BackingCallBack.filter(F.open_str == "student_utils"))
async def my_callback_foo(callback: CallbackQuery, callback_data: BackingCallBack, state: FSMContext):
    await state.clear()
    if callback_data.changing_pic:
        await callback.message.edit_media(InputMediaPhoto(media=str(pdc()[f"{callback_data.open_str}"][0]),
                                                          caption=str(pdc()[f"{callback_data.open_str}"][1]),
                                                          parse_mode='HTML'), reply_markup=utils())
    else:
        await callback.message.edit_caption(caption=str(pdc()[f"{callback_data.open_str}"][1]), parse_mode='HTML',
                                            reply_markup=utils())
