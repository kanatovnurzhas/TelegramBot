import telebot
#isagan
bot = telebot.TeleBot("2144718935:AAHD39CJRTLlPq9pQx9HBKzVWwEnH5zWDcc")
from telebot import types


@bot.message_handler(commands=["menu", "start"])
def button1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Расписание", "Platonus", "Инстаграм"]
    keyboard.add(*buttons)
    bot.send_message(message.from_user.id, text="Выбери", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def button(message):
    if message.text == "Platonus":
        keyboard = types.InlineKeyboardMarkup()
        key_plat = types.InlineKeyboardButton(text="Platonus", url="https://edu.enu.kz/template.html#/welcome")
        keyboard.add(key_plat)
        bot.send_message(message.from_user.id, text="Нажми на кнопку если хочешь перейти в Platonus",
                         reply_markup=keyboard)
    elif message.text == "Инстаграм":
        keyboard = types.InlineKeyboardMarkup()
        key_inst = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/nurzhaskanatov/")
        keyboard.add(key_inst)
        bot.send_message(message.from_user.id, text="Instagram", reply_markup=keyboard)
    elif message.text == "Расписание":
        keyboard = types.InlineKeyboardMarkup()
        key_pon = types.InlineKeyboardButton(text='Понедельник', callback_data="Понедельник")
        keyboard.add(key_pon)
        key_vtor = types.InlineKeyboardButton(text='Вторник', callback_data="Вторник")
        keyboard.add(key_vtor)
        key_sred = types.InlineKeyboardButton(text='Среда', callback_data="Среда")
        keyboard.add(key_sred)
        key_chet = types.InlineKeyboardButton(text='Четверг', callback_data="Четверг")
        keyboard.add(key_chet)
        key_pyat = types.InlineKeyboardButton(text='Пятница', callback_data="Пятница")
        keyboard.add(key_pyat)
        key_subb = types.InlineKeyboardButton(text='Суббота', callback_data="Суббота")
        keyboard.add(key_subb)
        bot.send_message(message.from_user.id, text="Выбери день недели", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Понедельник":
        bot.send_message(call.message.chat.id, text="Понедельник:\nБүгін демалыс, смело ұйықтай бер")
    elif call.data == "Вторник":
        bot.send_message(call.message.chat.id,
                         text="Вторник:\nКриптография-14:00-16:00\nОперационные системы-16:00-17:00")
    elif call.data == "Среда":
        bot.send_message(call.message.chat.id, text="Среда:\nКриптография-9:00-10:00")
    elif call.data == "Четверг":
        bot.send_message(call.message.chat.id,
                         text="Четверг:\nКриптография,'лаб'-8:00-10:00\nМетоды и средства защиты компьютерной "
                              "информации,'лек'-14:00-15:00\n"
                              "Менеджмент информационной безопасности,'лек'-15:00-17:00")
    elif call.data == "Пятница":
        bot.send_message(call.message.chat.id,
                         text="Пятница:\nТеория информации и кодирования,'прак'-8:00-10:00\nОперационные системы "
                              "и их безопасность,'лаб'-11:00-12:00\n"
                              "Менеджмент информационной безопасности,'лаб'-12:00-13:00\n"
                              "Теория информации и кодирования,'лек'-14:00-16:00 ")
    elif call.data == "Суббота":
        bot.send_message(call.message.chat.id, text="Суббота:\nМетоды и средства защиты "
                                                    "компьютерной информации,'лаб'-8:00-10:00\n"
                                                    "Операционные системы и их безопасность,'лаб'-10:00-11:00")


bot.polling(none_stop=True, interval=0)
