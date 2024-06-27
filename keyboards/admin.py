from aiogram import types
from aiogram.filters.callback_data import CallbackData

from keyboards.blinking import BackingCallBack


class AdminCallBack(CallbackData, prefix="nah"):  # goes to announcement.py
    action: str


def admin_panel():
    buttons = [
        [
            types.InlineKeyboardButton(text='Создать объявление', callback_data=AdminCallBack(action="announce").pack())
        ],
        [
            types.InlineKeyboardButton(text='Выйти из админ-панели',
                                       callback_data=BackingCallBack(changing_pic=True, open_str="main").pack())
        ]
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb


def announce_approve():
    buttons = [
        [
            types.InlineKeyboardButton(text='Подтвердить✅',
                                       callback_data=AdminCallBack(action="announce_approval").pack())
        ],
        [
            types.InlineKeyboardButton(text='⬅️Назад', callback_data=AdminCallBack(action="announce").pack())
        ]
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
