from aiogram import types
from aiogram.filters.callback_data import CallbackData


class MainTableCallBack(CallbackData, prefix="no"):  # goes to main_table.py
    changing_pic: bool
    open_str: str


def starting():
    buttons = [
        [
            types.InlineKeyboardButton(text='Способы подачи документов',
                                       callback_data=MainTableCallBack(changing_pic=True,
                                                                       open_str="applying_ways").pack()),
            # opens applying_ways page
            types.InlineKeyboardButton(text='Документы для поступления',
                                       callback_data=MainTableCallBack(changing_pic=True, open_str="docs").pack())
            # opens docs page
        ],
        [
            types.InlineKeyboardButton(text='Режим работы и контакты приёмной комиссии',
                                       callback_data=MainTableCallBack(changing_pic=True, open_str="priemn_com").pack())
            # opens priemn_com page
        ],
        [
            types.InlineKeyboardButton(text='Схема корпусов',
                                       callback_data=MainTableCallBack(changing_pic=True, open_str="scheme").pack()),
            # opens scheme page
            types.InlineKeyboardButton(text='Справочники абитуриента',
                                       callback_data=MainTableCallBack(changing_pic=True,
                                                                       open_str="helpers_obr_level").pack())
            # opens helpers page
        ],
        [
            types.InlineKeyboardButton(text='Общежития', callback_data=MainTableCallBack(changing_pic=True,
                                                                                         open_str="choose_dorm").pack())
            # opens dorm_choose page
        ],
        [
            types.InlineKeyboardButton(text="Для студента", callback_data=MainTableCallBack(changing_pic=True,
                                                                                            open_str="student_utils").pack())
        ]
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
