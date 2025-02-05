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



# show all the users

@router.message(IsAdmin(), Command('users'))
async def cmd_users(message: Message):
    await message.answer(f'The list of all users:\n{await rq.get_usernames()}')
