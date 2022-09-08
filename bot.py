from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def proces_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'привет\bчто будем делать?')

@dp.message_handler(commands=['help'])
async def proces_help(message: types.Message):
    await bot.send_message(message.from_user.id, 'нужна помощь?')

@dp.message_handler()
async def proces_reply(message: types.Message):
    await message.reply('ваш текст сообщения!')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)