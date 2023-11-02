import datetime
import random
import string

from colorama import Fore, Style
from unidecode import unidecode

from conversatio_modules import agradecimentos


# create logs from received msg
def registrar_log(mensagem):
    with open("log.txt", "a", encoding="utf-8") as arquivo_log:
        data_e_hora_atual = datetime.datetime.now()
        timestamp = data_e_hora_atual.strftime("%Y-%m-%d %H:%M:%S")
        arquivo_log.write(f"{timestamp}: {mensagem}\n")


# Remove special brazilian characteres ç ^´?...
def processar_mensagem(texto):
    # Remove caracteres especiais e acentos
    texto_processado = ''.join(char for char in unidecode(texto) if
                               char in string.ascii_letters or char in string.whitespace)
    # Converte para letras minúsculas
    texto_processado = texto_processado.lower()
    return texto_processado.strip()


# answer with a randon thanks
def responder_agradecimento():
    return random.choice(agradecimentos.respostas_aleatorias_agradecimento)

# create a prompt header
def header():
    text = 'Bot 4 Telegram'
    print(Fore.YELLOW + '=' * 40, Style.RESET_ALL)
    print(Fore.RED + ' '.join(text).upper(),
          Style.RESET_ALL)
    print(Fore.YELLOW + '=' * 40, Style.RESET_ALL)
    greetings = 'Welcome and enjoy'
    print(' '.join(greetings).upper())
    print(Fore.YELLOW + '-' * 40, Style.RESET_ALL)
