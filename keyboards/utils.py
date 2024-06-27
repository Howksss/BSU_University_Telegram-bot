from aiogram import types
from aiogram.filters.callback_data import CallbackData

from keyboards.blinking import BackingCallBack


class UtilCallBack(CallbackData, prefix="still_no"):  # goes to utils.py
    action: str


class PaginationCallBack(CallbackData, prefix="ahh not yet"):
    page: int


def utils():
    buttons = [
        [
            types.InlineKeyboardButton(text='Узнать баллы', callback_data=UtilCallBack(action="academ_points").pack())
        ],
        [
            types.InlineKeyboardButton(text='Уведомления о тестах',
                                       callback_data=UtilCallBack(action="tests_updates").pack())
        ],
        [
            types.InlineKeyboardButton(text='⬅️Назад', callback_data=BackingCallBack(changing_pic=True, open_str="main",
                                                                                     action="announce").pack())
        ]
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb


def academ_points():
    buttons = [
        [
            types.InlineKeyboardButton(text='✅Я согласен предоставить данные',
                                       callback_data=UtilCallBack(action="academ_points_login").pack())
        ],
        [
            types.InlineKeyboardButton(text='⬅️Назад',
                                       callback_data=BackingCallBack(changing_pic=True, open_str="student_utils",
                                                                     from_file=True).pack())
        ]
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb


def lk_balli_not_saved(page=0):
    buttons = [
        [
            types.InlineKeyboardButton(text="⬅", callback_data=PaginationCallBack(page=page - 1).pack()),
            types.InlineKeyboardButton(text="➡", callback_data=PaginationCallBack(page=page + 1).pack())
        ],
        [
            types.InlineKeyboardButton(text='Запомнить меня', callback_data=UtilCallBack(action="save_data").pack())
        ],
        [
            types.InlineKeyboardButton(text='⬅️Выйти',
                                       callback_data=BackingCallBack(changing_pic=True, open_str="student_utils",
                                                                     from_file=False).pack())
        ]
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb


def lk_balli_saved(page=0):
    buttons = [
        [
            types.InlineKeyboardButton(text="⬅", callback_data=PaginationCallBack(page=page - 1).pack()),
            types.InlineKeyboardButton(text="➡", callback_data=PaginationCallBack(page=page + 1).pack())
        ],
        [
            types.InlineKeyboardButton(text='Забыть меня', callback_data=UtilCallBack(action="forget_data").pack())
        ],
        [
            types.InlineKeyboardButton(text='⬅️Выйти',
                                       callback_data=BackingCallBack(changing_pic=True, open_str="student_utils",
                                                                     from_file=False).pack())
        ]
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
