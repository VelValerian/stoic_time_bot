from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.utils import *
from app.database import *
from app.keyboards import kb_reply


@dp.message(CommandStart())
async def cmd_start(message: Message):
    # await db_commands.db_start()
    await message.answer(f"Hi {message.from_user.username} "
                         "\n\nI'm a simple Bot that can store trivias in library."
                         "\nYou can store books or simple things that interest you.",
                         reply_markup=kb_reply.start_keyboard)
    await message.delete()


@dp.message(F.text == "Help")
async def cmd_help(message: Message):
    await message.answer("\nYou can BE BERET WITH THIS BOT!!!",
                         reply_markup=kb_reply.start_keyboard)
    await message.delete()


@dp.message(F.text.in_({"Begin", "Back"}))
async def cmd_begin(message: Message, state: FSMContext):
    await message.answer("Let's Start", reply_markup=kb_reply.begin_keyboard)
    await state.clear()
    await message.delete()


@dp.message(F.text == "Choose activity")
async def cmd_help(message: Message):
    await message.answer("Pick a topic of activity",
                         reply_markup=kb_reply.activity_keyboard)
    await message.delete()


