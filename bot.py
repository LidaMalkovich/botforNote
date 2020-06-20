
import telebot


import config
bot = telebot.TeleBot(config.token)
data = ''
password = ''

users = config.users
cursor = config.cursor
@bot.message_handler(commands=['start', 'help'])
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for user in users:
     # print(user[0])
     # print(user[1])

     keyboard.row(
        telebot.types.InlineKeyboardButton(str(user[0]), callback_data=user[0]+','+user[1])
     )
    bot.send_message(
        message.chat.id,
        'Click your login:',
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    global data
    print(query)
    data = str(query.data).split(',')
    print(data)
    get_ex_callback(query)


def get_ex_callback(query):
    bot.answer_callback_query(query.id)# убрать состояние загрузки
    send_exchange_result(query.message, query.data[4:])
def send_exchange_result(message, ex_code):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(
        message.chat.id, 'Введите пароль: '
    )
@bot.message_handler(content_types=["text"])
def default_test(message):
    print(message.text)
    print(data[1])
    if message.text == data[1]:
        bot.send_message(message.chat.id, 'Привет, '+ data[0])
        rest = sendForm(data[0])
        bot.send_message(message.chat.id, rest, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, 'Пароль неверный')

def sendForm(name):
    name = str("'"+name+"'");
    print(name)
    config.cursor.execute("SELECT * FROM note.users where name =%s" % str(name))
    # for row in cursor:
    #     print(row)
    records = config.cursor.fetchall() #возвращает все строки
    for row in records:
        print(row)
        userName = '<b>Имя пользователя: </b>'+ row[1] + '\n'+ '\n'

        dictData = row[3]
        infotext = ''
        cnt = 0;
        for t in list(dictData):
            cnt += 1
            print('t '+ str(t))
            thema ='<b>Тема:'+ str(cnt) +'</b>'+ '\n'+'<i>Наименование темы: </i>'+ '\n' + t["info"]+ \
                   '\n'+'<i>Текст: </i>'+ '\n' + t["theme"]
            infotext = infotext + thema + '\n' + '\n' + '\n'
        print(dictData)
    allInfo = userName + infotext
    print(allInfo)
    return allInfo

if __name__ == '__main__':
    bot.infinity_polling()