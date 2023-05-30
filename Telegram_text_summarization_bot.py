import os

# встановлення необхідних пакетів
os.system('pip install pyTelegramBotAPI')

import telebot
import json
import requests


# авторизація у системі власним Hugging Face токеном
headers = {"Authorization": f"Bearer MY_HUGGING_FACE_TOKEN"}

# URL до моделі text_summarization
SUM_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

# ініціалізація бота власним @BotFather токеном
bot = telebot.TeleBot("MY_TELEGRAM_BOT_TOKEN")



# запит до Hugging Face
def query(payload, URL):
    data = json.dumps(payload)
    response = requests.request("POST", URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


# дія бота на команду від користувача "/start"
@bot.message_handler(commands=['start'])
def start(msg):
    info = """
👋 Вітаю! 

🤖 Я - бот, що був створений для виконання NLP-завдань з використанням навчених моделей від Hugging Face 🤗. 

⚠️ Увага! На даний момент, моделі Hugging Face коректно працють лише з англійською мовою.

🧭 Введіть команду /text_summarization для узагальнення тексту."""
    bot.send_message(msg.chat.id, info)


# дія бота на команду від користувача "/text_summarization"
@bot.message_handler(commands=['text_summarization'])
def text_summarization(msg):
    info = """✍️ Будь ласка, введіть текст, який Ви хочете узагальнити:"""
    bot.send_message(msg.chat.id, info)
    
    # потім, коли ми отримуємо у відповідь текст, заходимо у цю функцію
    @bot.message_handler(content_types=['text'])
    def send_text(msg):
      info = """ 📝 Текст отримано. Інформація обробляється..."""
      bot.send_message(msg.chat.id, info)

      # відправляємо дані у модель text_summarization
      result = query(
        {"inputs": msg.text,
        "parameters": {"do_sample": False},
        },
        SUM_URL)

      info = """📩 Результат: """
      bot.send_message(msg.chat.id, info)

      # відправляємо результат користувачу  
      result = result[0]["summary_text"]
      bot.send_message(msg.chat.id, result)

    


# дія бота на команду від користувача "/help"
@bot.message_handler(commands=['help'])
def help_(msg):
    text = """
🪄 Доступні команди:

🔸 /text_summarization - узагальнення тексту
           """
    bot.send_message(msg.chat.id, text)



# запускаємо бота
if __name__ == "__main__":
  bot.polling()



