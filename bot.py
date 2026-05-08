import os
from aiogram import Bot, Dispatcher, types, executor

# Tokenni muhit o'zgaruvchisidan olamiz (Xavfsizlik uchun)
TOKEN = os.getenv("8411090193:AAG2laKqSafVIb1q5iTam0ttgw_m3b8OMPM")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Men CI/CD orqali ishga tushdim 🚀")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    print("Bot ishga tushmoqda...")
    executor.start_polling(dp, skip_updates=True)
