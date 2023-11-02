# List of answers when type TIPS
import random

dicas_list = [
    'Que tal tentar fazer uma pergunta diferente? ou clique /opcoes para ver umas lista!',
    'Experimente clicar /opcoes para obter uma lista de comandos disponíveis.',
    'Para obter informações sobre o bot, clique /opcoes para ver umas lista!',
    'Caso não encontre a resposta, clique /opcoes para ver umas lista!',
    'Você também pode clicar /opcoes para ver opções de conversa.',
]


# Função para responder com uma dica aleatória
def responder_dica():
    return random.choice(dicas_list)
