import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, OPENWEATHER_API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher()

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'

async def get_weather_in_moscow():
    params = {
        'id': 524901,  # ID Москвы
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric',  # Градусы Цельсия
        'lang': 'ru'        # Русский язык
    }
    timeout = aiohttp.ClientTimeout(total=10)  # Увеличенный таймаут
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(WEATHER_URL, params=params) as response:
            if response.status == 200:
                try:
                    return await response.json()
                except aiohttp.ContentTypeError:
                    return None  # Если формат ответа не JSON
            else:
                return None  # Ошибка, если статус не 200

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Добрый день! Слушаю тебя...')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help \n /weather')

@dp.message(Command('weather'))
async def weather(message: Message):
    weather_data = await get_weather_in_moscow()
    if weather_data:
        # Формируем сообщение о погоде
        city = weather_data['name']
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        weather_message = (
            f'Погода в городе {city}:\n'
            f'Температура: {temp}°C\n'
            f'Описание: {description.capitalize()}'
        )
        await message.answer(weather_message)
    else:
        await message.answer('Не удалось получить данные о погоде.')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())