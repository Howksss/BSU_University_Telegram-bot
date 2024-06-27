from aiogram import types
from aiogram.filters.callback_data import CallbackData

from keyboards.blinking import BackingCallBack


class HelpCallBack(CallbackData, prefix="no_yet"):  # goes to helpers.py
    empty: bool
    stage: int
    obr_level: str
    forma_obuch: str


def helpers_obr_level():
    buttons = [
        [
            types.InlineKeyboardButton(text='Магистратура',
                                       callback_data=HelpCallBack(empty=True, stage=1, obr_level="magistr",
                                                                  forma_obuch="").pack()),
            types.InlineKeyboardButton(text='Колледж',
                                       callback_data=HelpCallBack(empty=True, stage=1, obr_level="college",
                                                                  forma_obuch="").pack())
        ],
        [
            types.InlineKeyboardButton(text='Бакалавриат и специалитет',
                                       callback_data=HelpCallBack(empty=True, stage=1, obr_level="bakalavr_n_spec",
                                                                  forma_obuch="").pack())
        ],
        [
            types.InlineKeyboardButton(text='⬅️Назад',
                                       callback_data=BackingCallBack(changing_pic=True, open_str="main").pack())
        ]
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb


def helpers_forma_obuch(obr_level):
    if obr_level == "bakalavr_n_spec":
        buttons_bakalavr = [
            [
                types.InlineKeyboardButton(text='Очная', callback_data=HelpCallBack(empty=True, stage=2, obr_level="",
                                                                                    forma_obuch="ochn").pack()),
                types.InlineKeyboardButton(text='Заочная', callback_data=HelpCallBack(empty=True, stage=2, obr_level="",
                                                                                      forma_obuch="zaochn").pack())
            ],
            [
                types.InlineKeyboardButton(text='Очно-заочная дистанционная',
                                           callback_data=HelpCallBack(empty=True, stage=2, obr_level="",
                                                                      forma_obuch="ochn-zaochn").pack())
            ],
            [
                types.InlineKeyboardButton(text='⬅️Назад', callback_data=BackingCallBack(changing_pic=False,
                                                                                         open_str="helpers_obr_level").pack())
            ]
        ]
        kb_bakalavr = types.InlineKeyboardMarkup(inline_keyboard=buttons_bakalavr)
        return kb_bakalavr
    elif obr_level == "magistr":
        buttons_magistr = [
            [
                types.InlineKeyboardButton(text='Очная', callback_data=HelpCallBack(empty=True, stage=2, obr_level="",
                                                                                    forma_obuch="ochn").pack()),
                types.InlineKeyboardButton(text='Заочная', callback_data=HelpCallBack(empty=True, stage=2, obr_level="",
                                                                                      forma_obuch="zaochn").pack())
            ],
            [
                types.InlineKeyboardButton(text='Очная \n(с применением дистанционных технологий)',
                                           callback_data=HelpCallBack(empty=True, stage=2, obr_level="",
                                                                      forma_obuch="ochn_w_techs").pack())
            ],
            [
                types.InlineKeyboardButton(text='⬅️Назад', callback_data=BackingCallBack(changing_pic=False,
                                                                                         open_str="helpers_obr_level").pack())
            ]
        ]
        kb_magistr = types.InlineKeyboardMarkup(inline_keyboard=buttons_magistr)
        return kb_magistr
    elif obr_level == "college":
        buttons_college = [
            [
                types.InlineKeyboardButton(text='Очная', callback_data=HelpCallBack(empty=True, stage=2, obr_level="",
                                                                                    forma_obuch="ochn").pack()),
                types.InlineKeyboardButton(text='Заочная', callback_data=HelpCallBack(empty=True, stage=2, obr_level="",
                                                                                      forma_obuch="zaochn").pack())
            ],
            [
                types.InlineKeyboardButton(text='⬅️Назад', callback_data=BackingCallBack(changing_pic=False,
                                                                                         open_str="helpers_obr_level").pack())
            ]
        ]
        kb_college = types.InlineKeyboardMarkup(inline_keyboard=buttons_college)
        return kb_college
