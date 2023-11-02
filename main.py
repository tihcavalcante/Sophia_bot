# MaximBot for Telegram
#
# @author: <Tiago Cavalcante>
#
#
# Resume:
#
# The purpose of this bot is to provide automated responses to common questions,
# perform moderation of inappropriate messages, and interact with users through messages
# in private chats or groups. It uses a list of predefined answers to respond to questions,
# offers moderation of improper words, and can interact in both private chats and groups.
#
#
# This bot was designed to interact with Telegram Groups
#
import time
import telebot
from colorama import init
from conversatio_modules import news
from apiKeys.api import telegramKey
from functions.systemDef import *
from functions.conversation import responder
from functions.credits import Presentation

# Boot screen presentation
init()
print(Presentation)
header()

# Settings and Api Key
CHAVE_API = telegramKey
bot = telebot.TeleBot(CHAVE_API)


# Welcome message for new member in chat groups
@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def welcome(message):
    for member in message.new_chat_members:
        welcome_msg = f'''Olá, {member.first_name}! Seja bem-vindo ao grupo Maxim em Juiz de Fora!. Voce pode 
        digitar /opcoes para ver uma lista de perguntas sobre a Maxim.'''
        time.sleep(5)
        bot.send_message(message.chat.id, welcome_msg)


# search for daily news from chat
# to start the news service, you must type /noticias + word to search
@bot.message_handler(commands=["noticias"])
def obter_noticias_por_palavra_chave(mensagem):
    palavra_chave = mensagem.text.split("/noticias ", 1)[1]

    if palavra_chave:
        noticias = news.obter_noticias(palavra_chave)
        bot.send_message(mensagem.chat.id, noticias)
    else:
        bot.send_message(mensagem.chat.id, "Por favor, digite uma palavra-chave após o comando /noticias.")


# Processing messages received and respond
@bot.message_handler(func=lambda mensagem: True)
def processar_mensagem(mensagem):
    responder(mensagem)


def main():
    bot.polling()


# Auto relogin patch polling
if __name__ == '__main__':
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
