from aiogram import F, Router
from aiogram.types import CallbackQuery, InputMediaPhoto

from file_work.media_codesa import pdc
from keyboards.blinking import get_back_from_pam_dorm
from keyboards.dormitories import after_choosing_dorm, DormCallBack, get_back_from_geo

router = Router()


@router.callback_query(DormCallBack.filter(F.open_str == "desc"))
async def my_callback_foo(callback: CallbackQuery, callback_data: DormCallBack):
    await callback.message.edit_media(InputMediaPhoto(media=str(pdc()[f"dorm_{callback_data.dorm}"][0]),
                                                      caption=str(pdc()[f"dorm_{callback_data.dorm}"][1]),
                                                      parse_mode='HTML'),
                                      reply_markup=after_choosing_dorm(callback_data.dorm))


@router.callback_query(DormCallBack.filter(F.open_str == "geo"))
async def my_callback_foo(callback: CallbackQuery, callback_data: DormCallBack):
    await callback.message.answer_location(pdc()[f"dorm_{callback_data.dorm}"][2][0],
                                           pdc()[f"dorm_{callback_data.dorm}"][2][1], parse_mode='HTML',
                                           reply_markup=get_back_from_geo(callback_data.dorm))
    await callback.message.delete()


@router.callback_query(DormCallBack.filter(F.open_str == "pam_dorm"))
async def my_callback_foo(callback: CallbackQuery, callback_data: DormCallBack):
    await callback.message.answer_document(document=str(pdc()[f'{callback_data.open_str}'][0]),
                                           caption=str(pdc()[f'{callback_data.open_str}'][1]), parse_mode='HTML',
                                           reply_markup=get_back_from_pam_dorm())
    await callback.message.delete()
