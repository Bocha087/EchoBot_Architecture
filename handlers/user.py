from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from aiogram import Router

router = Router()

@router.message(Command(commands='start'))
async def start_command(message:Message):
    await message.answer(text=LEXICON_RU['/start'])

@router.message(Command(commands='help'))
async def help_command(message:Message):
    await message.answer(text=LEXICON_RU['/help'])