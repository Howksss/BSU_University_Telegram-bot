from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery

from file_work.media_codesa import pdc
from keyboards.blinking import helper
from keyboards.helpers import HelpCallBack, helpers_forma_obuch

router = Router()


class Helpers_choose(StatesGroup):
    obr_level = State()
    obuch_form = State()


@router.callback_query(HelpCallBack.filter(F.empty == True))
async def helpers_magistr(callback: CallbackQuery, callback_data: HelpCallBack, state: FSMContext):
    if callback_data.stage == 1:
        await state.update_data(obr_level=callback_data.obr_level)
        await callback.message.edit_caption(caption=str(pdc()["helpers_obr_level"][1]), parse_mode='HTML',
                                            reply_markup=helpers_forma_obuch(callback_data.obr_level))
    elif callback_data.stage == 2:
        await state.update_data(obuch_form=callback_data.forma_obuch)
        ident_helper = await state.get_data()
        await callback.message.answer_document(
            document=str(pdc()[f"{ident_helper['obr_level']}_{ident_helper['obuch_form']}"][0]),
            caption=str(pdc()["helpers_end"][1]), parse_mode='HTML', reply_markup=helper())
        await callback.message.delete()
