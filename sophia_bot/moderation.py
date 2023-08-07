# moderacao.py
# swear words list
palavras_improprias = [
"puta", "piranha", "safada", "xoxota", "put@", 'merda', 'bosta', 'merd@', 'lixo', 'buceta', 'tomar no cu',
'putinha', 'chupar', 'piroca','fuder', 'foda', 'porra', 'caralho', 'crl', 'caraio', 'porra', 'viado', 'pqp', 'filha da puta',
]

def moderar_mensagem(mensagem):
    texto = mensagem.text.lower()
    
    for palavra in palavras_improprias:
        if palavra in texto:
            return True  
    
    return False  