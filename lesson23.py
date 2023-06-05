import os
import logging
import random

from aiogram import Bot, Dispatcher, executor, types

from decouple import config

API_TOKEN = config('TELEGRAM_BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

b_cat = types.KeyboardButton('😽🙀Котик')

main_keyboard = types.ReplyKeyboardMarkup()
main_keyboard.add(b_cat)


users = [
    
]




@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    text = 'Прівіт, радий тебе бачити!\n\n' \
            'Якщо ти хочеш дізнатися, що я вмію, то напиши /help'
    await message.reply(text, reply_markup=main_keyboard)

    
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply("Я бот для навчання Python. Поки що я вмію тільки це.")


@dp.message_handler(commands=['kb1'])
async def kb1_command(message: types.Message):
    markup = types.ReplyKeyboardMarkup(row_width=6)
    markup.add('👍')
    markup.add('👎','👊')
    markup.insert('👊')
    markup.insert('👍')
    markup.insert('👎')
    markup.insert('👎')
    markup.insert('👎')
    markup.insert('👎')
    markup.insert('👎')
    markup.insert('👎')
    markup.insert('👎')
    markup.insert('👎')
    markup.row('👍')
    markup.insert('👎')
    markup.row('🤏', '👎')
    await message.answer("Як тобі цей бот?", reply_markup=markup)

@dp.message_handler(commands=['kb2'])
async def kb1_command(message: types.Message):
    markup = types.ReplyKeyboardMarkup(row_width=6)
    b_cont = types.KeyboardButton('Відправити свій контакт', request_contact=True)
    markup.add(b_cont)
    await message.answer("Надішли свій контакт", reply_markup=markup)
    
@dp.message_handler(content_types=['contact'])
async def contact_handler(message: types.Message):
    print(message.contact)
    await message.answer(f"Твій номер телефону: {message.contact.phone_number}")

@dp.message_handler(commands=['kb3'])
async def kb1_command(message: types.Message):
    markup = types.ReplyKeyboardMarkup(row_width=6)
    b_geo = types.KeyboardButton('Відправити своє місцезнаходження', request_location=True)
    markup.add(b_geo)
    await message.answer("Надішли своє місцезнаходження", reply_markup=markup)
    
@dp.message_handler(content_types=['location'])
async def location_handler(message: types.Message):
    print(message.location)
    await message.answer(f"Твої координати: {message.location.latitude}, {message.location.longitude}")

@dp.message_handler(commands=['kb4'])
async def kb1_command(message: types.Message):
    inline_btn_1 = types.InlineKeyboardButton('fghdfgdsfgdfgsdfgsdfgsdfg dfgsdfg!', callback_data='button11')
    inline_btn_2 = types.InlineKeyboardButton('Друга кнопка!', callback_data='button22')
    inline_kb1 = types.InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)
    await message.answer("Натисни на кнопку", reply_markup=inline_kb1)

@dp.callback_query_handler(text='button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Натиснув на першу кнопку')
    
@dp.callback_query_handler(text='button2')
async def process_callback_button2(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Натиснув на другу кнопку')

# @dp.message_handler(commands=['kb5'])
# async def kb1_command(message: types.Message):
    
#     inline_kb1 = types.InlineKeyboardMarkup()
    
#     await message.answer("Натисни на кнопку", reply_markup=inline_kb1)

@dp.message_handler(commands=['reg'])
async def reg_command(message: types.Message):
    users.append(dict(message.from_user))
    print(users)

@dp.message_handler(commands=['users'])
async def users_command(message: types.Message):    
    # text = []
    # for user in users:
    #     text.append(f"{user.get('id')} - {user.get('first_name')} {user.get('last_name')} @{user.get('username')}")
    markup = types.InlineKeyboardMarkup()
    for user in users:
        markup.add(types.InlineKeyboardButton(f"{user.get('first_name')} {user.get('last_name')}", callback_data=f"user_{user.get('id')}"))
    await message.answer(f"Список користувачів:\n", reply_markup=markup)

# @dp.callback_query_handler(lambda c: c.data.startswith('user_'))
@dp.callback_query_handler(text_startswith='user_')
async def process_callback_button1(callback_query: types.CallbackQuery):
    
    await callback_query.answer('Вибрано користувача', show_alert=True)
    
    
    text ='Ви вибрали користувача:\n'
    # user_1
    user_id = int(callback_query.data.split('_')[1])
    for user in users:
        if user.get('id') == user_id:
            text += f"{user.get('first_name')} {user.get('last_name')}- @{user.get('username')}"
            break
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Видалити', callback_data=f"del_{user_id}"))
    markup.add(types.InlineKeyboardButton('КОтик', url='https://w.forfun.com/fetch/70/7047b702475924ba8f8044b5b5ca56ba.jpeg'))
    markup.add(types.InlineKeyboardButton('lms', url='https://lms.ithillel.ua/'))
    
    await callback_query.message.edit_text(text, reply_markup=markup)


@dp.message_handler(commands=['delreply'])
async def delreply_command(message: types.Message):
    await message.answer('llala kb del' , reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['test'])
async def users_command(message: types.Message):  
    text = ''
    for i in range(500):
        text += f"{i}\n"
    await message.answer(text)

@dp.message_handler()
async def echo(message: types.Message):
    print(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    

