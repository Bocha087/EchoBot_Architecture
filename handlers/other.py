from aiogram.types import Message
from aiogram import Router
from lexicon.lexicon import LEXICON_RU

router = Router()

@router.message()
async def other_message(message:Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text = LEXICON_RU['no_echo'])