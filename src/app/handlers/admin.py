import app.keyboards as k
from app.database import requests as rq
from app.filters import IsAdmin

import logging
import asyncio

from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()



# stopping the bot

@router.message(IsAdmin(), F.text.casefold() == 'stop')
async def cmd_stop(message: Message, bot: Bot):
    await message.answer('Stopping the bot... ⛓️‍💥')
    logging.warning('Stopping the bot...')

    loop = asyncio.get_event_loop()
    loop.stop()
    await bot.session.close()
    logging.warning('Bot Stopped')


# show all the users

@router.message(IsAdmin(), Command('users'))
async def cmd_users(message: Message):
    await message.answer(f'The list of all users:\n{await rq.get_usernames()}')
