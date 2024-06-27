from aiogram import types
from aiogram.filters.callback_data import CallbackData


class BackingCallBack(CallbackData, prefix="also_no"):  # goes to blinking.py
    changing_pic: bool
    from_file: bool = False
    open_str: str


def get_back(with_or_not: bool):
    buttons = [[
        types.InlineKeyboardButton(text='⬅️Назад',
                                   callback_data=BackingCallBack(from_file=False, changing_pic=with_or_not,
                                                                 open_str="main").pack())
    ]]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb


def get_back_from_pam_dorm():
    buttons = [[
        types.InlineKeyboardButton(text='⬅️Назад', callback_data=BackingCallBack(from_file=True, changing_pic=True,
                                                                                 open_str="choose_dorm").pack())
    ]]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb


def helper():
    buttons = [
        [
            types.InlineKeyboardButton(text='⏮В главное меню', callback_data=BackingCallBack(changing_pic=True,
                                                                                             open_str="from_helpers_to_main").pack())
        ]
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb


def announce():
    buttons = [
        [
            types.InlineKeyboardButton(text='⬅️Назад',
                                       callback_data=BackingCallBack(changing_pic=True, open_str="admin_panel").pack())
        ]
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
