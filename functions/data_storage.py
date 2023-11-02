# if you want to create a data_storage to start training AI
import json


def salvar_dados_em_arquivo(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo)


def carregar_dados_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
