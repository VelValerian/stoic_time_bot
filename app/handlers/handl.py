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
async def cmd_begin(message: Message):
    await message.answer("Let's Start", reply_markup=kb_reply.begin_keyboard)
    await message.delete()


@dp.message(F.text == "Choose activity")
async def cmd_help(message: Message):
    await message.answer("Pick a topic of activity",
                         reply_markup=kb_reply.activity_keyboard)
    await message.delete()


@dp.message(F.text == "Stop")
async def cmd_help(message: Message):
    await message.answer("You press STOP buttons",
                         reply_markup=kb_reply.begin_keyboard)
    await message.delete()


@dp.message(F.text == "Rest")
async def cmd_help(message: Message):
    await message.answer("Pick activity",
                         reply_markup=kb_reply.rest_keyboard)
    await message.delete()


@dp.message(F.text == "Health")
async def cmd_help(message: Message):
    await message.answer("Pick activity",
                         reply_markup=kb_reply.health_keyboard)
    await message.delete()


@dp.message(F.text == "Routine")
async def cmd_help(message: Message):
    await message.answer("Pick activity",
                         reply_markup=kb_reply.routine_keyboard)
    await message.delete()


@dp.message(F.text == "Study")
async def cmd_help(message: Message):
    await message.answer("Pick activity",
                         reply_markup=kb_reply.study_keyboard)
    await message.delete()


@dp.message(F.text == "Job")
async def cmd_help(message: Message):
    await message.answer("Pick activity",
                         reply_markup=kb_reply.job_keyboard)
    await message.delete()


@dp.message(F.text == "Road to")
async def cmd_help(message: Message):
    await message.answer("Pick activity",
                         reply_markup=kb_reply.road_keyboard)
    await message.delete()


@dp.message(F.text.in_({"Watching", "Read", "Game", "Sleep", "Food",
                        "Party", "Hobby", "Short break", "Meditation",
                        "Yoga", "Fitness", "Warm-up", "Outdoor",
                        "Morning", "Evening", "Doctor", "Analyses",
                        "Cooking", "Cleaning", "Repairing", "Shopping",
                        "Reading", "Videos", "Learning", "Coding", "At work",
                        "At home", "To work", "To home", "To study", "To meeting",
                        "To party / hobby / fun"}))
async def cmd_begin(message: Message):
    await message.answer("Press Stop when complete activity", reply_markup=kb_reply.stop_keyboard)
    await message.delete()


@dp.message(F.text == "Sports exercises")
async def cmd_help(message: Message):
    await message.answer("Pick activity",
                         reply_markup=kb_reply.health_sports_keyboard)
    await message.delete()


@dp.message(F.text == "Health routine")
async def cmd_help(message: Message):
    await message.answer("Pick activity",
                         reply_markup=kb_reply.health_routine_keyboard)
    await message.delete()


@dp.message(F.text == "Health care")
async def cmd_help(message: Message):
    await message.answer("Pick activity",
                         reply_markup=kb_reply.health_care_keyboard)
    await message.delete()
