import asyncio
import random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

AVATAR_STYLES = [
    'adventurer', 'adventurer-neutral', 'avataaars', 'bottts',
    'croodles', 'croodles-neutral', 'fun-emoji', 'identicon',
    'initials', 'micah', 'miniavs', 'open-peeps', 'pixel-art', 'pixel-art-neutral'
]

def get_random_avatar():
    style = random.choice(AVATAR_STYLES)
    avatar_url = f'https://api.dicebear.com/9.x/{style}/png?seed={random.randint(1, 10000)}'
    return avatar_url


@dp.message(Command("avatar"))
async def send_avatar(message: Message):
    avatar_url = get_random_avatar()
    await message.answer_photo(photo=avatar_url)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
