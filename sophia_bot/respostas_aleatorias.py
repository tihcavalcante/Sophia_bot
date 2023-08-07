import random
# respostas_aleatorias.py
#
# random answers list
#
# You should call this function on conversation.py
#
#
respostas_list = [
'Sua busca por conhecimento é inspiradora. Estou aqui para ajudar no que precisar.',
'Sua curiosidade é a chama que alimenta meu desejo de aprender e ajudar.',
'Sua curiosidade é contagiosa, e estou animada para explorar novos temas com você.',
]

# Função para responder com uma resposta aleatória
def responder_aleatoriamente():
    return random.choice(respostas_list)
