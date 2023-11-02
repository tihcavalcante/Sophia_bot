# MaximBot for telegram
# 
# @author: <Tiago Cavalcante>
#
# 
# import library
import logging
import time
import telebot
from apiKeys.api import telegramKey
from conversatio_modules import dicas
from conversatio_modules.help import ajuda
from conversatio_modules.qa import palavras_chave_respostas
from conversatio_modules.talk_list import small_talk
from functions import cooldown
from functions.moderation import moderar_mensagem
from functions.systemDef import *
from colorama import Fore, Style

# Registry of your bot API KEY given by BotFather
CHAVE_API = telegramKey
bot = telebot.TeleBot(CHAVE_API)

# Regitry settings log registry - Configuração do registro de log
logging.basicConfig(format="%(asctime)s - %(name)s - "
                           "%(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# set cooldown time
COOLDOWN_TIME = 3


def encontrar_ajuda(pergunta):
    for chave, resposta in ajuda.items():
        if chave in pergunta:
            return resposta
    return None


# Find answers on QA.py
def encontrar_resposta_especial(pergunta):
    for chave, resposta in palavras_chave_respostas.items():
        if chave.lower() in pergunta:
            return resposta
    return None


# Find the answer on the list talklist.py
def encontrar_resposta(pergunta):
    for resposta in small_talk:
        if pergunta in resposta.lower():
            return resposta
    return None


# Module process start
@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    pergunta = processar_mensagem(mensagem.text.strip())
    registrar_log(mensagem.text)
    resposta = encontrar_resposta(pergunta)
    resposta_especial = encontrar_resposta_especial(pergunta)
    resposta_ajuda = encontrar_ajuda(pergunta)
    # print different colors for receveid msg
    print(Fore.YELLOW + f"Mensagem recebida: {pergunta}", Style.RESET_ALL)

    # Moderation function action settings in the module moderation.py
    if moderar_mensagem(mensagem):
        # If message contains blacklisted words bot should send an alert in chat
        bot.delete_message(mensagem.chat.id, mensagem.message_id)
        # Delete blacklisted words from chat
        bot.send_message(mensagem.chat.id,
                         "Sua mensagem contém palavras impróprias. "
                         "Por favor, evite o uso de linguagem inadequada.")

    # answer in the module help.py bot wil send in chats
    elif resposta_ajuda is not None:
        time.sleep(6)  # Delay msg
        bot.send_message(mensagem.chat.id, resposta_ajuda)
        print(f"Mensagem enviada: {resposta_ajuda}")

    # if answer was found in the module qa.py bot wil send in chats
    elif resposta_especial is not None:
        time.sleep(6)  # Delay msg
        bot.send_message(mensagem.chat.id, resposta_especial)
        print(f"Mensagem enviada: {resposta_especial}")

    # if answer in module talk_list.py bot wil send in chats
    elif resposta is not None:
        time.sleep(5)  # Delay msg
        bot.send_message(mensagem.chat.id, resposta)
        print(f"Mensagem enviada: {resposta}")

    # verifies if question is in "dicas"
    elif "dicas" in pergunta:
        time.sleep(7)  # Delay msg
        resposta = dicas.responder_dica()
        bot.send_message(mensagem.chat.id, resposta)
        print(f"Mensagem enviada: {resposta}")

    # check if text is an acknowledgment
    elif ("thanks" in pergunta or "obrigado" in pergunta or "obg"
          in pergunta or "tks" in pergunta or "thanx" in pergunta):
        time.sleep(8)
        resposta = responder_agradecimento()
        bot.send_message(mensagem.chat.id, resposta)
        print(f"Mensagem enviada: {resposta}")

    # ignore sucessive msgs, reply only after COOLDOWN_TIME
    user_id = mensagem.from_user.id
    if cooldown.has_cooldown(user_id, COOLDOWN_TIME):
        return

    else:
        pass
