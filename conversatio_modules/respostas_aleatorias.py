import random

# Here type your random list of commom answers you want to provide
# if there's no answer ))))

respostas_list = [
    'A aprendizagem é uma jornada constante, e estou feliz de tê-lo como parte dela.',
    'A aprendizagem é uma viagem emocionante, e estou feliz que você esteja aqui comigo.',
    'A cada nova pergunta, estou mais preparada para ajudar e fornecer informações precisas.',
    'A cada nova questão, tenho a oportunidade de ser uma assistente ainda mais completa.',
    'A cada pergunta, meu conhecimento se expande. Obrigado por ser parte disso.',
    'A curiosidade é o combustível para o aprendizado contínuo. Continue questionando!',
    'A jornada do conhecimento é infinita, e estou pronta para explorar cada etapa.',
]


# Função para responder com uma resposta aleatória
def responder_aleatoriamente():
    return random.choice(respostas_list)
