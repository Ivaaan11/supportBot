import app.keyboards as k
import app.database.requests as rq
from app import utils

import logging as log

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



# create ticket

class Ticket(StatesGroup):
    confirm = State()
    name = State()
    text = State()


@router.message(Command('ticket'))
async def create_ticket(message: Message, state: FSMContext):
    await message.answer('Do you want to create a ticket?', reply_markup=k.yes_no_keyboard())
    await state.set_state(Ticket.confirm)


@router.callback_query(Ticket.confirm, F.data == 'no')
async def cancel_ticket(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Canceled')
    await state.clear()


@router.callback_query(Ticket.confirm, F.data == 'yes')
async def sure_ticket(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Enter a name for the ticket')
    await state.set_state(Ticket.name)


@router.message(Ticket.name)
async def ticket_name(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await message.answer(f"Your ticket's name is <b>{message.text}</b>", parse_mode='HTML')
    await message.answer('Describe your problem')
    await state.set_state(Ticket.text)


@router.message(Ticket.text)
async def ticket_text(message: Message, state: FSMContext):
    await state.update_data(text = message.text)
    data = await state.get_data()
    name = data.get('name')
    await message.answer(f'So, your ticket is: \n<b>{name}</b>\n{message.text}', parse_mode='HTML')
    await state.clear()



# echo

@router.message()
async def echo_message(message: Message):
    await message.answer('Unknown command 🤔\nType /help to view the list of commands')
    log.info('echo message')

@router.callback_query()
async def echo_callback(callback: CallbackQuery):
    await callback.answer()
    log.info('echo callback')
