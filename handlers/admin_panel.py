import os

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

from file_work.media_codesa import pdc
from keyboards.admin import admin_panel

router = Router()


@router.message(Command(commands=["admin"]))
async def my_callback_foo(message: Message):
    load_dotenv()
    if message.from_user.id == int(os.getenv('ADMIN')):
        await message.answer_photo(photo=str(pdc()["admin_panel"][0]), caption=str(pdc()["admin_panel"][1]),
                                   parse_mode='HTML', reply_markup=admin_panel())
