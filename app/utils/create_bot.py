from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

load_dotenv()
token = os.environ.get('TG_TOKEN')
bot = Bot(token=token, parse_mode="HTML")
dp = Dispatcher()
