import app.keyboards as k
import app.database.requests as rq
from app import utils

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()



# starting the bot and main navigation

@router.message(Command('start'))
async def cmd_start(message: Message):
    await rq.add_new_user(message.from_user.id, message.from_user.username)
    await message.answer(f'Hello {message.from_user.first_name}! 👋')


@router.message(Command('menu'))
async def cmd_menu(message: Message):
    await message.answer('💻 Main menu')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f'📱 Available commands:\n{utils.display_commands()}')



# echo

@router.message()
async def echo_message(message: Message):
    await message.answer('Unknown command 🤔\nType /help to view the list of commands')

@router.callback_query()
async def echo_callback(callback: CallbackQuery):
    await callback.answer()
