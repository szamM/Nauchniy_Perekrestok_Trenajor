import telebot
from telebot import types
import random
token = '5725444903:AAFtKsFenV6t_mHu2AzDT7AGvA2D0y7QUe4'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    greeting = f'Привет, {message.from_user.first_name}, чтобы начать решать варианты нажми на кнопку ❇ Перейти к подготовке! ❇'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    reg = types.KeyboardButton('❇ Перейти к подготовке! ❇')
    connect_with_me = types.KeyboardButton('✉Связаться с cоздателем✉')
    markup.add(reg, connect_with_me)
    bot.send_message(message.chat.id, greeting, reply_markup=markup)


@bot.message_handler()
def checker(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    connect_with_me = types.KeyboardButton('✉Связаться с cоздателем✉')
    apart = types.KeyboardButton('🧮 Прорешивать отдельные задания 🧮')
    all_var = types.KeyboardButton('💯 Решить вариант 💯')
    dop_m = types.InlineKeyboardMarkup()
    an_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    global back_cool
    back_cool = types.KeyboardButton('🔙 Назад 🔙')
    global n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11
    n1 = types.KeyboardButton('①')
    n2 = types.KeyboardButton('②')
    n3 = types.KeyboardButton('③')
    n4 = types.KeyboardButton('④')
    n5 = types.KeyboardButton('⑤')
    n6 = types.KeyboardButton('⑥')
    n7 = types.KeyboardButton('⑦')
    n8 = types.KeyboardButton('⑧')
    n9 = types.KeyboardButton('⑨')
    n10 = types.KeyboardButton('⑩')
    n11 = types.KeyboardButton('⑪')
    dop_m.add(types.InlineKeyboardButton("🔴", url="https://vk.com/szamaxin"))
    if message.text == '🔙 Назад 🔙':
        markup.add(apart, all_var, connect_with_me)
        bot.send_message(message.chat.id, '🔙✅ Вернулся назад ✅🔙', reply_markup=markup)
    if message.text == '✉Связаться с cоздателем✉':
        bot.send_message(message.chat.id, "⬇ Нажими на кнопку ⬇", reply_markup=dop_m)
    if message.text == '❇ Перейти к подготовке! ❇':
        markup.add(apart, all_var, connect_with_me)
        bot.send_message(message.chat.id, "Отлично! Теперь выбери как ты хочешь готовиться!", reply_markup=markup)
    if message.text == '🧮 Прорешивать отдельные задания 🧮':
        an_markup.add(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, back_cool)
        bot.register_next_step_handler(message, apart_numbers)
        bot.send_message(message.chat.id, 'Теперь выбери номер задания!', reply_markup=an_markup)
    if message.text == '🔙 Вернуться к списку задач 🔙':
        an_markup.add(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, back_cool)
        bot.send_message(message.chat.id, '🔙✅ Вернулся к списку задач ✅🔙', reply_markup=an_markup)
        bot.register_next_step_handler(message, apart_numbers)
    if message.text == '💯 Решить вариант 💯':
        an_markup.add(n1, n2, n3, back_cool)
        bot.register_next_step_handler(message, solve_of_variants)
        bot.send_message(message.chat.id, 'Теперь выбери номер варианта!\nPS: Учти, что у тебя не получиться изменить вариант ответа, так что придется сразу вписывать правильные ответы', reply_markup=an_markup)
    if message.text == 'Вернуться к списку вариантов!':
        an_markup.add(n1, n2, n3, back_cool)
        bot.register_next_step_handler(message, solve_of_variants)


def editor(message, answer_list):
    if message.text == '🏁 Узнать результаты решений 🏁':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        backi = types.KeyboardButton('Вернуться к списку вариантов!')
        markup.add(backi)
        number_of_good_answers = 0
        an = []
        for i in range(len(answer_list)):
            if list_of_answ[i] == answer_list[i]:
                number_of_good_answers += 1
            else:
                an.append(str(i + 1))
        if len(an) == 0:
            bot.send_message(message.chat.id, '🎉 Поздравляю ты решил все без ошибок 🎉', reply_markup=markup)
            bot.register_next_step_handler(message, solve_of_variants)
        elif len(an) == 1:
            wrongs = ('').join(an)
            bot.send_message(message.chat.id, f'К сожалению ты допустил {len(wrongs)} ошибку в задании {wrongs}.', reply_markup=markup)
            bot.register_next_step_handler(message, solve_of_variants)
        else:
            wrongs = (', ').join(an)
            bot.send_message(message.chat.id, f'К сожалению ты допустил ошибки в следующих заданиях: {wrongs}.', reply_markup=markup)
            bot.register_next_step_handler(message, solve_of_variants)
    else:
        bot.register_next_step_handler(message, editor, answer_list=answer_list)


def variant_res(message, variant, answer_list):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    finish = types.KeyboardButton('🏁 Узнать результаты решений 🏁')
    if len(variant) == 0:
        list_of_answ.append(message.text)
        markup.add(finish)
        bot.send_message(message.chat.id, 'Ты решил вариант, теперь у тебя есть возможность узнать свои ошибки или изменить выбранные ответы', reply_markup=markup)
        bot.register_next_step_handler(message, editor, answer_list=answer_list)
    else:
        if message.text == 'Вернуться к списку вариантов!':
            markup.add(n1, n2, n3, back_cool)
            bot.send_message(message.chat.id, 'Вернулся к списку вариантов', reply_markup=markup)
            bot.register_next_step_handler(message, solve_of_variants)
        else:
            back_to_var = types.KeyboardButton('Вернуться к списку вариантов!')
            markup.add(back_to_var)
            list_of_answ.append(message.text)
            bot.send_photo(message.chat.id, open(variant[0], 'rb'), reply_markup=markup)
            bot.register_next_step_handler(message, variant_res, variant=variant, answer_list=answer_list)
            variant.pop(0)


def solve_of_variants(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    mmark = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    connect_with_me = types.KeyboardButton('✉Связаться с cоздателем✉')
    apart = types.KeyboardButton('🧮 Прорешивать отдельные задания 🧮')
    all_var = types.KeyboardButton('💯 Решить вариант 💯')
    markup.add(apart, all_var, connect_with_me)
    back = types.KeyboardButton('🔙 Вернуться к списку вариантов 🔙')
    markup_an = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_an.add(back)
    var_1_answers = ['7,5', '4', '0,5', '0,992', '1,2', '2', '3', '5', '90', '-7', '20']
    var_2_answers = ['60', '360', '0,408', '0,8', '3,25', '10', '-2', '2', '20', '-9', '0']
    var_3_answers = ['7', '125', '0,392', '1,25', '6', '5', '0', '0,2', '10', '2', '5']
    global list_of_answ
    list_of_answ = []
    global variant1
    variant1 = ["E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant1\\number1.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant1\\number2.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant1\\number3.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant1\\number4.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant1\\number5.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant1\\number6.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant1\\number7.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant1\\number8.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant1\\number9.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant1\\number10.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant1\\number11.png"]
    global variant2
    variant2 = ["E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant2\\number1.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant2\\number2.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant2\\number3.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant2\\number4.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant2\\number5.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant2\\number6.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant2\\number7.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant2\\number8.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant2\\number9.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant2\\number10.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant2\\number11.png"]
    global variant3
    variant3 = ["E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant3\\number1.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant3\\number2.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant3\\number3.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant3\\number4.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant3\\number5.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant3\\number6.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant3\\number7.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant3\\number8.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant3\\number9.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant3\\number10.png",
                "E:\\Nauchniy_Perekrestok_Trenajor\\variants\\variant3\\number11.png"]
    markup_an = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    back_to_var = types.KeyboardButton('Вернуться к списку вариантов!')
    markup_an.add(back_to_var)
    if message.text == '🔙 Назад 🔙':
        bot.send_message(message.chat.id, '🔙✅ Вернулся назад! ✅🔙', reply_markup=markup)
    if message.text == 'Вернуться к списку вариантов!':
        mmark.add(n1, n2, n3, back_cool)
        bot.register_next_step_handler(message, solve_of_variants)
        bot.send_message(message.chat.id, '🔙✅ Вернулся к списку вариантов! ✅🔙', reply_markup=mmark)
    if message.text == '①':
        bot.register_next_step_handler(message, variant_res, variant=variant1, answer_list=var_1_answers)
        bot.send_photo(message.chat.id, open(variant1[0], 'rb'), reply_markup=markup_an)
        variant1.pop(0)
    if message.text == '②':
        bot.register_next_step_handler(message, variant_res, variant=variant2, answer_list=var_2_answers)
        bot.send_photo(message.chat.id, open(variant2[0], 'rb'), reply_markup=markup_an)
        variant2.pop(0)
    if message.text == '③':
        bot.register_next_step_handler(message, variant_res, variant=variant3, answer_list=var_3_answers)
        bot.send_photo(message.chat.id, open(variant3[0], 'rb'), reply_markup=markup_an)
        variant3.pop(0)


def tracking(message, listt):
    back = types.KeyboardButton('🔙 Вернуться к списку задач 🔙')
    markup_an = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_an.add(back)
    if len(listt) > 0:
        path_answer = listt[0].split('!')
        answer = path_answer[1]
        if ',' in answer:
            answer = answer.split(',')
            answer = [answer[0] + ',' + answer[1], answer[0] + '.' + answer[1]]
        an_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        if message.text == '🔙 Вернуться к списку задач 🔙':
            an_markup.add(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, back_cool)
            bot.send_message(message.chat.id, '🔙✅ Вернулся к списку задач ✅🔙', reply_markup=an_markup)
            bot.register_next_step_handler(message, apart_numbers)
        else:
            if message.text not in ['Решить еще одну одиннадцатую задачу', 'Решить еще одну десятую задачу', 'Решить еще одну девятую задачу',
                     'Решить еще одну восьмую задачу', 'Решить еще одну седьмую задачу', 'Решить еще одну шестую задачу','Решить еще одну пятую задачу',
                     'Решить еще одну четвертую задачу', 'Решить еще одну третью задачу', 'Решить еще одну вторую задачу', 'Решить еще одну первую задачу']:
                if message.text in answer:
                    bot.send_message(message.chat.id, 'Поздравляю, ты ответил правильно!')
                    bot.register_next_step_handler(message, tracking, listt=listt)
                    if len(listt) > 0:
                        listt.pop(0)
                    else:
                        bot.send_message(message.chat.id, 'Задачи закончились', reply_markup=markup_an)
                else:
                    bot.send_message(message.chat.id, 'Ты допустил ошибку')
                    bot.register_next_step_handler(message, tracking, listt=listt)
            else:
                if len(listt) > 0:
                    listt.pop(0)
                    if len(listt) > 0:
                        path_answer = listt[0].split('!')
                        bot.send_photo(message.chat.id, open(path_answer[0], 'rb'))
                        bot.register_next_step_handler(message, tracking, listt=listt)
                    else:
                        bot.send_message(message.chat.id, 'Задачи закончились', reply_markup=markup_an)
                else:
                    bot.send_message(message.chat.id, 'Задачи закончились', reply_markup=markup_an)
    else:
        bot.send_message(message.chat.id, 'Задачи закончились', reply_markup=markup_an)


def apart_numbers(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    connect_with_me = types.KeyboardButton('✉Связаться с cоздателем✉')
    apart = types.KeyboardButton('🧮 Прорешивать отдельные задания 🧮')
    all_var = types.KeyboardButton('💯 Решить вариант 💯')
    markup.add(apart, all_var, connect_with_me)
    #
    next_number_1 = types.KeyboardButton('Решить еще одну первую задачу')
    next_number_2 = types.KeyboardButton('Решить еще одну вторую задачу')
    next_number_3 = types.KeyboardButton('Решить еще одну третью задачу')
    next_number_4 = types.KeyboardButton('Решить еще одну четвертую задачу')
    next_number_5 = types.KeyboardButton('Решить еще одну пятую задачу')
    next_number_6 = types.KeyboardButton('Решить еще одну шестую задачу')
    next_number_7 = types.KeyboardButton('Решить еще одну седьмую задачу')
    next_number_8 = types.KeyboardButton('Решить еще одну восьмую задачу')
    next_number_9 = types.KeyboardButton('Решить еще одну девятую задачу')
    next_number_10 = types.KeyboardButton('Решить еще одну десятую задачу')
    next_number_11 = types.KeyboardButton('Решить еще одну одиннадцатую задачу')
    #
    back = types.KeyboardButton('🔙 Вернуться к списку задач 🔙')
    markup_an_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_an_1.add(next_number_1, back)
    markup_an_2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_an_2.add(next_number_2, back)
    markup_an_3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_an_3.add(next_number_3, back)
    markup_an_4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_an_4.add(next_number_4, back)
    markup_an_5 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_an_5.add(next_number_5, back)
    markup_an_6 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_an_6.add(next_number_6, back)
    markup_an_7 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_an_7.add(next_number_7, back)
    markup_an_8 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_an_8.add(next_number_8, back)
    markup_an_9 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_an_9.add(next_number_9, back)
    markup_an_10 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_an_10.add(next_number_10, back)
    markup_an_11 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_an_11.add(next_number_11, back)
    #
    another_mark = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    another_mark.add(back_cool)
    global ex1
    ex1 = ['E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y1\\y1.png!5',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y1\\y2.png!8',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y1\\y3.png!4',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y1\\y4.png!9,6',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y1\\y5.png!8',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y1\\y6.png!24',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y1\\y7.png!1',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y1\\y8.png!18',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y1\\y9.png!21',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y1\\y10.png!30',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y1\\y11.png!3',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y1\\y12.png!1',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y1\\y13.png!100']
    global ex2
    ex2 = ['E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y2\\y1.png!4',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y2\\y2.png!48',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y2\\y3.png!132',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y2\\y4.png!7',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y2\\y5.png!5',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y2\\y6.png!2',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y2\\y7.png!75',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y2\\y8.png!3',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y2\\y9.png!1',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y2\\y10.png!9',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y2\\y11.png!14']
    global ex3
    ex3 = ['E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y3\\y1.png!0,25',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y3\\y2.png!0,33',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y3\\y3.png!0,1',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y3\\y5.png!0,2',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y3\\y6.png!0,006',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y3\\y7 - Copy.png!0,25']
    global ex4
    ex4 = ['E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y4\\y2.png!0,64',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y4\\y3.png!0,43',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y4\\y4.png!5',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y4\\y6.png!0,8',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y4\\y7.png!0,125']
    global ex5
    ex5 = ['E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y5\\y1.png!-7',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y5\\y2.png!5',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y5\\y3.png!87',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y5\\y4.png!4',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y5\\y5.png!-124']
    global ex6
    ex6 = ['E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y6\\y1.png!80',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y6\\y2.png!6',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y6\\y3.png!2',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y6\\y4.png!4',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y6\\y5.png!1,5']
    global ex7
    ex7 = ['E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y7\\y1.png!20',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y7\\y2.png!-0,25',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y7\\y3.png!-7',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y7\\y4.png!6',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y7\\y5.png!1,25']
    global ex8
    ex8 = ['E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y8\\y1.png!1',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y8\\y2.png!10',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y8\\y3.png!180000',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y8\\y4.png!30',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y8\\y5.png!0,0025']
    global ex9
    ex9 = ['E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y9\\y1.png!530000',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y9\\y2.png!7',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y9\\y3.png!108',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y9\\y4.png!616',
           'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y9\\y5.png!6']
    global ex10
    ex10 = ['E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y10\\y1.png!-0,75',
            'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y10\\y2.png!3',
            'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y10\\y3.png!20',
            'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y10\\y4.png!4',
            'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y10\\y5.png!2',
            'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y10\\y6.png!4,75']
    global ex11
    ex11 = ['E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y11\\y1 - Copy.png!-2',
            'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y11\\y2.png!10',
            'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y11\\y3.png!-18',
            'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y11\\y4.png!5',
            'E:\\Nauchniy_Perekrestok_Trenajor\\apart_numbers\\y11\\y5.png!1']

    random.shuffle(ex1)
    random.shuffle(ex2)
    random.shuffle(ex3)
    random.shuffle(ex4)
    random.shuffle(ex5)
    random.shuffle(ex6)
    random.shuffle(ex7)
    random.shuffle(ex8)
    random.shuffle(ex9)
    random.shuffle(ex10)
    random.shuffle(ex11)

    global file11
    file11 = ex11[0].split('!')
    global file10
    file10 = ex10[0].split('!')
    global file9
    file9 = ex9[0].split('!')
    global file8
    file8 = ex8[0].split('!')
    global file7
    file7 = ex7[0].split('!')
    global file6
    file6 = ex6[0].split('!')
    global file5
    file5 = ex5[0].split('!')
    global file4
    file4 = ex4[0].split('!')
    global file3
    file3 = ex3[0].split('!')
    global file2
    file2 = ex2[0].split('!')
    global file1
    file1 = ex1[0].split('!')
    if message.text == '🔙 Назад 🔙':
        bot.send_message(message.chat.id, '🔙✅ Вернулся назад ✅🔙', reply_markup=markup)
    if message.text == '①':
        bot.register_next_step_handler(message, tracking, listt=ex1)
        bot.send_photo(message.chat.id, open(file1[0], 'rb'), reply_markup=markup_an_1)
    if message.text == '②':
        bot.register_next_step_handler(message, tracking, listt=ex2)
        bot.send_photo(message.chat.id, open(file2[0], 'rb'), reply_markup=markup_an_2)
    if message.text == '③':
        bot.register_next_step_handler(message, tracking, listt=ex3)
        bot.send_photo(message.chat.id, open(file3[0], 'rb'), reply_markup=markup_an_3)
    if message.text == '④':
        bot.register_next_step_handler(message, tracking, listt=ex4)
        bot.send_photo(message.chat.id, open(file4[0], 'rb'), reply_markup=markup_an_4)
    if message.text == '⑤':
        bot.register_next_step_handler(message, tracking, listt=ex5)
        bot.send_photo(message.chat.id, open(file5[0], 'rb'), reply_markup=markup_an_5)
    if message.text == '⑥':
        bot.register_next_step_handler(message, tracking, listt=ex6)
        bot.send_photo(message.chat.id, open(file6[0], 'rb'), reply_markup=markup_an_6)
    if message.text == '⑦':
        bot.register_next_step_handler(message, tracking, listt=ex7)
        bot.send_photo(message.chat.id, open(file7[0], 'rb'), reply_markup=markup_an_7)
    if message.text == '⑧':
        bot.register_next_step_handler(message, tracking, listt=ex8)
        bot.send_photo(message.chat.id, open(file8[0], 'rb'), reply_markup=markup_an_8)
    if message.text == '⑨':
        bot.register_next_step_handler(message, tracking, listt=ex9)
        bot.send_photo(message.chat.id, open(file9[0], 'rb'), reply_markup=markup_an_9)
    if message.text == '⑩':
        bot.register_next_step_handler(message, tracking, listt=ex10)
        bot.send_photo(message.chat.id, open(file10[0], 'rb'), reply_markup=markup_an_10)
    if message.text == '⑪':
        bot.register_next_step_handler(message, tracking, listt=ex11)
        bot.send_photo(message.chat.id, open(file11[0], 'rb'), reply_markup=markup_an_11)


def main():
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()