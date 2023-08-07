#!/usr/bin/env python
#
# @author: <Tiago Cavalcante https://github.com/tihcavalcante>
# This bot was designed to interact with Telegram Group
# 
#
# This program is free software: you can redistribute it and/or modify
# it under the terms OF MIT License.
#
# This program is distributed in the hope that it will be useful for study and updgrades.
# The purpose of this bot is to provide automated responses to common questions, 
# perform moderation of inappropriate messages, and interact with users through messages 
# in chats or groups. It uses a list of predefined answers to respond to questions, 
# offers moderation of improper words, and can interact in both private chats and groups.
#
#
#

import telebot
import time
from conversation import responder
from colorama import init, Fore, Style
from credits import Presentation
import telebot, time
import news
# Boot screen presentation 
init()
print(Presentation)

frase = 'PRINT A WELCOME MSG ON THE OPEN SCREEN'
print(Fore.YELLOW + '=' * 40, Style.RESET_ALL) # Fore insere a cor no texto, style Reseta a cor
print(Fore.RED + ' '.join(frase).upper(), Style.RESET_ALL) # insere = entre os caracteres # Fore insere a cor no texto, style Reseta a cor
print(Fore.YELLOW + '=' * 40, Style.RESET_ALL) # Fore insere a cor no texto, style Reseta a cor
saudacao = 'Welcome and enjoy'
print(' '.join(saudacao).upper())
print(Fore.YELLOW +'-' * 40, Style.RESET_ALL)
#--------------------------------------------

# Settings and Api Key
CHAVE_API = ""YOUR TELEGRAM API BOT KEY""
bot = telebot.TeleBot(CHAVE_API)
# Welcome message for new member in chat
@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def boas_vindas(message):
    for member in message.new_chat_members:
        boas_vindas_msg = f'''Olá, {member.first_name}! 
Meu nome é Sophia,
e serei sua companheira para tirar algumas dúvidas de como trabalhar na Maxim, 
Seja bem-vindo ao grupo Maxim em Juiz de Fora!. 
Voce pode digitar /opcoes para ver uma lista de perguntas sobre a Maxim.'''
        time.sleep(5)  # delay 5 seconds
        bot.send_message(message.chat.id, boas_vindas_msg)

# search for daily news from chat
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
# Auto relogin patch polling problem
if __name__=='__main__':
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
