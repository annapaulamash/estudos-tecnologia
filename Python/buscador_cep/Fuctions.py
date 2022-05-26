
import requests
import json
 

#função que buscar cep  e retornar o endereço
def buscar_cep(cep):   
    if len(cep) == 8:
        busca = requests.get("https://cep.awesomeapi.com.br/json/{}".format(cep))
        return status_code(busca,cep)   
    else:
        busca = requests.get("https://cep.awesomeapi.com.br/json/{}".format(cep))
        return status_code(busca,cep)

#funcao para desenvolver as mensagens e os objetos de retorno
def status_code(busca,cep):
    if busca.status_code == 200:
        text = """
        Este é o CEP inserido: {}
        Nosso status code é: {}
        Nosso objeto Json retornado é:\n {}""".format(cep, busca.status_code, busca.json())
        return text
    elif busca.status_code == 404:
        text = """
        Este é o CEP inserido: {}
        Nosso status code é: {}
        Nosso objeto Json retornado é: {}""".format(cep, busca.status_code, busca.json())
        return text
    elif busca.status_code == 400:
        text = """
        Este é o CEP inserido: {}
        Nosso status code é: {} é inválido
        Nosso objeto Json retornado é: {}""".format(cep, busca.status_code, busca.json())
        return text
       




    












