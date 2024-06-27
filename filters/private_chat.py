from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsPrivate(BoundFilter):
    async def chat_type(self, message: types.Message):
        return message.chat.type == types.Chat.type
