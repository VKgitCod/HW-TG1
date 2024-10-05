import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import TOKEN

import kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Поехали!", reply_markup=kb.hw1)

@dp.message(F.text == "Привет!")
async def test_button(message: Message):
   await message.answer(f'Привет, {message.from_user.full_name}!')

@dp.message(F.text == "Пока.")
async def test_button(message: Message):
   await message.answer(f'До свидания, {message.from_user.full_name}!')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n1. /start \n2. /help \n3. /links \n4. /dynamic')

@dp.message(Command('links'))
async def links(message: Message):
    await message.answer('Тебе доступно', reply_markup=kb.inline_hw2)

@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer('Кое что еще', reply_markup=kb.inline_hw3)

@dp.callback_query(F.data == 'change')
async def change(callback: CallbackQuery):
   await callback.answer("Кнопки изменяются...", show_alert=True)
   await callback.message.edit_text('Новые возможности', reply_markup=await kb.choice())

@dp.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())