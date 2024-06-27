from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message, InputMediaPhoto

from database.sqlite import Database
from file_work.media_codesa import pdc
from keyboards.blinking import get_back
from keyboards.main_table import starting
from keyboards.utils import UtilCallBack, lk_balli_saved
from keyboards.utils import academ_points
from scripts.balli import get_points

router = Router()
db = Database()


class RegisterState(StatesGroup):
    RegLog = State()
    RegPass = State()
    trash = State()


@router.callback_query(UtilCallBack.filter(F.action == "academ_points"))
async def my_callback_foo(callback: CallbackQuery, callback_data: UtilCallBack):
    result = db.data_extsts(callback.from_user.id)
    if not (result[0][2] != None and result[0][3] != None):
        await callback.message.edit_media(InputMediaPhoto(media=str(pdc()[f"{callback_data.action}"][0]),
                                                          caption=str(pdc()[f"{callback_data.action}"][1]),
                                                          parse_mode='HTML'), reply_markup=academ_points())
    else:
        data = {'RegLog': f'{result[0][2]}',
                'RegPass': f'{result[0][3]}'}
        print(data)
        answer = "---------------------------------------------------\n"
        academs = []
        for key, arg in get_points(data["RegLog"], data["RegPass"]).items():
            answer += f'<b>{key}</b>:   {arg}\n'
            academs.append(f'{key}: {arg}')
        pages = len(academs) / 15
        await callback.message.edit_media(
            media=InputMediaPhoto(media=str(pdc()["academ_points_creating_acc"][0]), caption=answer, parse_mode='HTML'),
            reply_markup=lk_balli_saved()
        )


@router.callback_query(UtilCallBack.filter(F.action == "academ_points_login"))
async def my_callback_foo(callback: CallbackQuery, callback_data: UtilCallBack, state: FSMContext):
    await callback.message.edit_media(InputMediaPhoto(media=str(pdc()[f"{callback_data.action}"][0]),
                                                      caption=str(pdc()[f"{callback_data.action}"][1]),
                                                      parse_mode='HTML'), reply_markup=get_back(
        True))
    await state.set_state(RegisterState.RegLog)


@router.message(RegisterState.RegLog, F.text)
async def my_callback_foo(message: Message, state: FSMContext):
    await state.update_data(RegLog=message.text)
    await message.answer_photo(photo=str(pdc()[f"academ_points_password"][0]),
                               caption=str(pdc()[f"academ_points_password"][1]), parse_mode='HTML',
                               reply_markup=get_back(True))
    await state.set_state(RegisterState.RegPass)


@router.message(RegisterState.RegPass, F.text)
async def my_callback_foo(message: Message, state: FSMContext):
    await state.update_data(RegPass=message.text)
    data = await state.get_data()
    answer = "---------------------------------------------------\n"
    for key, arg in get_points(data["RegLog"], data["RegPass"]).items():
        answer += f'<b>{key}</b>:   {arg}\n'
    if get_points(user_log=data["RegLog"], user_pass=data["RegPass"]) != {}:

        await state.set_state(RegisterState.trash)
    elif get_points(user_log=data["RegLog"], user_pass=data["RegPass"]) == {}:
        await message.answer_photo(photo=str(pdc()["academ_points_wrong"][0]),
                                   caption=str(pdc()["academ_points_wrong"][1]), parse_mode='HTML',
                                   reply_markup=get_back(True))
        await state.set_state(RegisterState.trash)


@router.callback_query(UtilCallBack.filter(F.action == "save_data"))
async def my_callback_foo(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    db.save_data(data["RegLog"], data["RegPass"], callback.from_user.id)
    await callback.message.edit_reply_markup(reply_markup=lk_balli_saved())


@router.callback_query(UtilCallBack.filter(F.action == "forget_data"))
async def my_callback_foo(callback: CallbackQuery, callback_data: UtilCallBack, state: FSMContext):
    db.forget_data(callback.from_user.id)
    await callback.message.edit_media(InputMediaPhoto(media=str(pdc()[f"{callback_data.action}"][0]),
                                                      caption=str(pdc()[f"{callback_data.action}"][1]),
                                                      parse_mode='HTML'), reply_markup=get_back(
        True))
    await state.set_state(RegisterState.RegLog)


@router.message(RegisterState.trash)
async def my_callback_foo(message: Message):
    await message.answer_photo(photo=str(pdc()["main"][0]), caption=str(pdc()["main"][1]), parse_mode='HTML',
                               reply_markup=starting())
