from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


hw1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет!")], [KeyboardButton(text="Пока.")]
], resize_keyboard=True)

inline_hw2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url='https://dzen.ru/news/?utm_referrer=yandex.ru')],
    [InlineKeyboardButton(text="Музыка", url='https://vk.com/audio-2001319413_8319413')],
    [InlineKeyboardButton(text="Видео", url='https://vk.com/video?z=video-219465931_456240156%2Fpl_cat_trends')]
])

inline_hw3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data='change')],
])

variables = ["Опция 1", "Опция 2"]

async def choice():
    keybord = InlineKeyboardBuilder()
    for key in variables:
        keybord.add(InlineKeyboardButton(text=key, url="https://vk.com/video/movies?z=video-203654344_456239865%2Fpl_-207536086_28"))
    return keybord.adjust(2).as_markup()

