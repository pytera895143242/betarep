import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

TOKEN = '5515088482:AAHp20iSg7MJdHiF3mtDbhCjcw4S33qAWy8'
memory_storage = MemoryStorage()

bot = Bot(token=TOKEN,parse_mode='html',disable_web_page_preview=True)
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)