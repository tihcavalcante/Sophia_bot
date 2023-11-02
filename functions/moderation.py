# moderation of swearwords

palavras_improprias = [
    "puta", "piranha", "safada", "xoxota", "put@", 'maxim lixo',
    'maxim é lixo', 'app lixo', 'merda', 'bosta', 'merd@', 'lixo', 'buceta', 'tomar no cu',
    'putinha', 'chupar', 'piroca', 'mobil', 'up master', 'indriver', 'uber', 'vrumm',
    'fuder', 'foda', 'porra', 'caralho', 'crl', 'caraio', 'porra', 'pior app', 'censura', 'bolsonaro', 'lula',
    'petista',
    'viado', 'pqp', 'filha da puta',
]


def moderar_mensagem(mensagem):
    texto = mensagem.text.lower()

    for palavra in palavras_improprias:
        if palavra in texto:
            return True  # Mensagem contém uma palavra imprópria

    return False  # Mensagem não contém palavras impróprias
