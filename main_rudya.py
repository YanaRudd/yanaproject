import bs4
import telebot
import requests
link = 'https://yandex.ru/pogoda/'
response = requests.get(link)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
bot = telebot.TeleBot("-")
# with open('tmp.html', 'w') as file:
   # file.write(response.text)
cards = list(soup.find_all('ul', {'class': 'swiper-wrapper'})[1].children)[:7]
weather = []
for card in cards:
    info = {}
    divs = card.findAll('div')
    degrees_day = divs[1].text
    if '+' in degrees_day:
        degrees_day = int(degrees_day[degrees_day.find('+'):])
    else:
        degrees_day = -int(degrees_day[degrees_day.find('-'):])
    degrees_night = divs[2].text
    if '+' in degrees_night:
        degrees_night = int(degrees_night[degrees_night.find('+'):])
    else:
        degrees_night = -int(degrees_night[degrees_night.find('-'):])
    info['date'] = divs[0].text
    info['day'] = degrees_day
    info['night'] = degrees_night
    info['precipetation'] = divs[3].text
    weather.append(info)

for elem in weather:
    print(elem)

print(type(info))

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет, вы за погодой?")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Я бот умный, но у меня одна функция: говорить вам погодку в России-матушке. Списочек команд: /start /help /pogoda")


@bot.message_handler(commands=['pogoda'])
def pogoda(message):
    bot.send_message(message.chat.id, f'\n{weather[0]["date"]}: Днем {weather[0]["day"]} , Ночью {weather[0]["night"]} , {weather[0]["precipetation"]}'
                                     f'\n{weather[1]["date"]}: Днем {weather[1]["day"]} , Ночью {weather[1]["night"]} , {weather[1]["precipetation"]}'
                                      f'\n{weather[2]["date"]}: Днем {weather[2]["day"]} , Ночью {weather[2]["night"]} , {weather[2]["precipetation"]}'
                                      f'\n{weather[3]["date"]}: Днем {weather[3]["day"]} , Ночью {weather[3]["night"]} , {weather[3]["precipetation"]}'
                                      f'\n{weather[4]["date"]}: Днем {weather[4]["day"]} , Ночью {weather[4]["night"]} , {weather[4]["precipetation"]}'
                                      f'\n{weather[5]["date"]}: Днем {weather[5]["day"]} , Ночью {weather[5]["night"]} , {weather[5]["precipetation"]}'
                                      f'\n{weather[6]["date"]}: Днем {weather[6]["day"]} , Ночью {weather[6]["night"]} , {weather[6]["precipetation"]}')


#Сегодня: Днем 6, Ночью -2, Ясно
#Воскресенье: Днем 9, Ночью -4, Пасмурно



@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if  message.text == 'Да':
        bot.reply_to(message, 'Будет сделано, пожалуйста,  введите "/pogoda"')
    elif message.text == 'yes':
        bot.reply_to(message, 'Братан, а кто Берлин взял, по-русски можно?')
    elif message.text == 'Нет':
        bot.reply_to(message, 'Ну так я большего и не умею. Ты по названию не понял что ли?')
    elif message.text == 'Погода':
        bot.reply_to(message, 'Вот погода на сегодня: ')
    else:
        bot.reply_to(message, 'Вы точно это хотите сказать?')



bot.polling()