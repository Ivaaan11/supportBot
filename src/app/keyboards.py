from aiogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup
)
from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    KeyboardBuilder
)



# Reply keyboards

def repl_kb() -> ReplyKeyboardMarkup:
    builder = KeyboardBuilder()

    builder.add(KeyboardButton(text='Template text'))

    return builder.as_markup(one_time_keyboard = True)



# Inline keyboards

def inln_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text='Template inline', callback_data='template_callback')

    return builder.as_markup()


def yes_no_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text='yes ✅', callback_data='yes')
    builder.button(text='no ❌', callback_data='no')

    return builder.as_markup()


# payments

def payment_kb(price) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text = f'pay {price} XTR', pay = True))

    return builder.as_markup()
