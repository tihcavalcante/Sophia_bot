import requests

# Chave de API da NewsAPI.org
API_KEY = "f0d1743f52ef45749fc5a779eaae6d0d"

def obter_noticias(palavra_chave):
    url = f"http://newsapi.org/v2/everything?q={palavra_chave}&apiKey={API_KEY}"
    response = requests.get(url)
    dados = response.json()

    if response.status_code == 200 and dados["totalResults"] > 0:
        noticias = ""
        for noticia in dados["articles"]:
            titulo = noticia["title"]
            url_noticia = noticia["url"]
            noticias += f"\n- {titulo} ({url_noticia})"
            
        # Limitar respostas a 4096 caracteres
        max_response_length = 4096
        if len(noticias) > max_response_length:
            noticias = noticias[:max_response_length]    

        return noticias
    else:
        return "Nenhuma notícia encontrada."

