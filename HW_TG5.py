import asyncio
import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import TOKEN
from googletrans import Translator

dp = Dispatcher()
bot = Bot(token=TOKEN)

translator = Translator()

def get_random_advice():
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        response.raise_for_status()
        advice_data = response.json()
        advice = advice_data.get('slip', {}).get('advice', 'Совет не найден.')

        translated_advice = translator.translate(advice, dest='ru').text
        return translated_advice
    except requests.exceptions.RequestException as e:
        return "Не удалось получить совет. Попробуйте позже."

@dp.message(Command("council"))
async def council(message: Message):
    advice = get_random_advice()
    await message.answer(advice)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
