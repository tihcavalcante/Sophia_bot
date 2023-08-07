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
#
#
#
import telebot, time
import datetime
from datetime import datetime
import dicas
import thanks
import logging
import time
from datetime import datetime
from talk_list import small_talk
from moderation import moderar_mensagem
from colorama import init, Fore, Style
from qa import palavras_chave_respostas
from help import help
import unidecode
import string
import cooldown

# Registry of your bot API KEY given by BotFather
CHAVE_API = "YOUR TELEGRAM API BOT KEY"
bot = telebot.TeleBot(CHAVE_API)
# Regitry settings log registry - Configuração do registro de log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

COOLDOWN_TIME = 15
# Text color function
init()

# Function to create log file and log messages
def registrar_log(mensagem):
    with open("log.txt", "a", encoding="utf-8") as arquivo_log:
        data_e_hora_atual = datetime.now()
        timestamp = data_e_hora_atual.strftime("%Y-%m-%d %H:%M:%S")
        arquivo_log.write(f"{timestamp}: {mensagem}\n")

# Remove special brazilian characteres ç ^´?
def processar_mensagem(texto):
    # Remove special brazilian characteres
    texto_processado = ''.join(char for char in unidecode.unidecode(texto) if char in string.ascii_letters or char in string.whitespace)
    # convert to lower case
    texto_processado = texto_processado.lower()
    return texto_processado.strip()

# Function to find keywords in the question and return the corresponding answer from QA
def encontrar_resposta_especial(pergunta):
    for chave, resposta in palavras_chave_respostas.items():
        if chave.lower() in pergunta: 
            return resposta
    return None  

# Find the answer on the list Small Talk
def encontrar_resposta(pergunta):
    for resposta in small_talk:
        if pergunta in resposta.lower(): 
            return resposta
    return None

def encontrar_ajuda(pergunta):
    for chave, resposta in help.items():
        if chave in pergunta:
            return resposta
    return None 

# Module process start
@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    registrar_log(mensagem.text)
    pergunta = processar_mensagem(mensagem.text.strip())
    resposta = encontrar_resposta(pergunta)
    resposta_especial = encontrar_resposta_especial(pergunta)
    resposta_ajuda = encontrar_ajuda(pergunta) 
 
# Moderation function action settings in the module moderation.py    
    if moderar_mensagem(mensagem):
        # If message contains blacklisted words bot should send an alert in chat
        bot.delete_message(mensagem.chat.id, mensagem.message_id)  # Delete blacklisted words from chat
        bot.send_message(mensagem.chat.id, "Sua mensagem contém palavras impróprias. Por favor, evite o uso de linguagem inadequada.") # you can change the 'message'

# answer was found in the module qa.py bot wil send in chats  
    elif resposta_especial is not None:
        time.sleep(30)  # Delay msg
        bot.send_message(mensagem.chat.id, resposta_especial)
                
# answer in module talk_list.py bot wil send in chats        
    elif resposta is not None:
        time.sleep(30) 
        bot.send_message(mensagem.chat.id, resposta)

# answer in the module help.py bot wil send in chats  
    elif resposta_ajuda is not None:
        time.sleep(6)
        bot.send_message(mensagem.chat.id, resposta_ajuda)
       
# Verify if question is on dicas.py
    elif "dicas" in pergunta:
        time.sleep(7)  # Delay msg
        resposta = dicas.responder_dica()
        bot.send_message(mensagem.chat.id, resposta)
        
# Verify if question is on thanks.py
    elif "obrigado" in pergunta or "agradecido" in pergunta or "obg" in pergunta or "obrigadu" in pergunta or "thanks" in pergunta or "grato" in pergunta or "grata" in pergunta or "obrigada" in pergunta or "agradecida" in pergunta or 'vc e 10' in pergunta or 'voce e muito gentil' in pergunta or "valeu" in pergunta or "tmj" in pergunta or "vlw" in pergunta or "jae" in pergunta or "mandou bem" in pergunta or "show de bola" in pergunta:
        time.sleep(15)  # Delay msg
        resposta = thanks.answer_thanks()
        bot.send_message(mensagem.chat.id, resposta)
     
#--ignore sucessive msgs from 1 client, reply only after COOLDOWN_TIME change the time wait
    user_id = mensagem.from_user.id
    if cooldown.has_cooldown(user_id, COOLDOWN_TIME):
        return

# If bot didnt find any answer should provide an answer from bellow or none.

# Grettings Messages
    elif "bom dia" in pergunta or "saudações" in pergunta or "buenos dias" in pergunta or "bomdia" in pergunta:
        time.sleep(30)  # Atraso de 10 segundos
        bot.send_message(mensagem.chat.id, "Bom dia, como você está?, se quiser algumas respostas, voce pode clicar /opcoes para mais informações!")
  
    elif "qual e o seu nome" in pergunta or 'qual o seu nome' in pergunta or 'como voce se chama' in pergunta or 'como vc chama' in pergunta or 'como vc chama' in pergunta:
            time.sleep(15)  # Atraso de 20 segundos
            bot.send_message(
                mensagem.chat.id, '''My name is Sophia 💋,
I will be your guide on how to work with the App!!

How can I help??

You can type /options !''')
        
    else:
    #    time.sleep(5)  # Atraso de 1 dia
    #    bot.send_message(mensagem.chat.id, respostas_aleatorias.responder_aleatoriamente())  #if you wish you can use respostas_aleatorias.py (random answers) for questions without answer yet
        pass

    print(Fore.YELLOW + f"Mensagem recebida: {pergunta}", Style.RESET_ALL)
    print("Resposta Enviada:", resposta, resposta_especial, resposta_ajuda) # this command print on the screen the questions and answers from telegram bot interactions
