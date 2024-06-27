from aiogram import types
from aiogram.filters.callback_data import CallbackData

from keyboards.blinking import BackingCallBack


class DormCallBack(CallbackData, prefix="still_no"):  # goes to dormitories.py
    dorm: int
    open_str: str


def get_back_from_geo(num: int):
    buttons = [[
        types.InlineKeyboardButton(text='⬅️Назад', callback_data=DormCallBack(dorm=num, open_str=f"dorm_{num}").pack())
    ]]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb


def choose_dorm():
    nums = [1, 2, 3, 5]
    buttons = []
    for x in nums:
        buttons.append([types.InlineKeyboardButton(text=f"Общежитие №{x}",
                                                   callback_data=DormCallBack(dorm=x, open_str="desc").pack())])
    buttons.append([types.InlineKeyboardButton(text='Памятка о заселении в общежитие',
                                               callback_data=DormCallBack(dorm=0, open_str="pam_dorm").pack())])
    buttons.append([types.InlineKeyboardButton(text='⬅️Назад', callback_data=BackingCallBack(changing_pic=True,
                                                                                             open_str="main").pack())])
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb


def after_choosing_dorm(num: int):
    buttons = [
        [
            types.InlineKeyboardButton(text='📍Расположение на карте',
                                       callback_data=DormCallBack(dorm=num, open_str="geo").pack())
        ],
        [
            types.InlineKeyboardButton(text='⬅️Назад',
                                       callback_data=BackingCallBack(changing_pic=True, open_str="choose_dorm").pack())
        ]]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
