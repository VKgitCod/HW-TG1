import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN
import random
from googletrans import Translator

bot = Bot(token=TOKEN)
dp = Dispatcher()

translator = Translator()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Добрый день, {message.from_user.full_name}!')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n1. /start \n2. /help \n3. /voice \n4. Так же он сохранит отправленную ему картинку \n5. Если же ему что то написать, он переведет это на английский язык')

@dp.message(F.photo)
async def reakt_photo(message: Message):
    await message.answer('Ваша картинка сохранена :)')
    await bot.download(message.photo[-1], destination=f'pict/{message.photo[-1].file_id}.jpg')

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://avatars.mds.yandex.net/i?id=faf0764508cb1d5e9e2c885929b361d88def6392-5194823-images-thumbs&n=13',
            'https://avatars.mds.yandex.net/i?id=43e7339a210df0fa161f706ffdd7a46d13bcbc2c-6951238-images-thumbs&ref=rim&n=33&w=397&h=350',
            'https://avatars.mds.yandex.net/i?id=031eebeac63aa32b81d6dec4007b08c88012da3f-9229664-images-thumbs&ref=rim&n=33&w=480&h=270'
            ]
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='а вот и картинка')

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile("sample.ogg")
    await message.answer_voice(voice)


@dp.message()
async def translate_message(message: Message):
    text = message.text
    translated = translator.translate(text, dest='en').text
    await message.answer(translated)

@dp.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())