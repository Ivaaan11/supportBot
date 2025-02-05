from aiogram.types import BotCommand


commands = [
    BotCommand(command = 'start', description = 'Start the bot'),
    BotCommand(command = 'menu', description = 'View the main menu'),
    BotCommand(command = 'help', description = 'View all the available commands'),
]


def display_commands():
    answer = ''

    for command in commands:
        command = str(command).split("'")
        answer = f'{answer}\n/{command[1]} - {command[3]}'
    
    return answer
