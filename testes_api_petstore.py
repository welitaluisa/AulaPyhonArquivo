from wsgiref import headers

import pytest
import requests

url = 'https://petstore.swagger.io/v2/user'

def testar_incluir_usuario():
    # configura
    status_code_esperado = 200  # comunicação
    code_esperado = 200  # funcional
    type_esperado = 'unknown'  # fixo como desconhecido
    mensagem_esperada = '3421'

    headers = {'Content-Type': 'application/json'}
    resposta = requests.post(url = url,
                             data=open('json/usuario1.json', 'rb'),
                             headers=headers
                             )
    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_consulta_usuario():
    # configura

    username = 'welita' # input / entrada para consulta
    id_esperado = 3421
    username_esperado = 'welita'
    email_esperado = 'socorro@teste.com'
    telefone_esperado = '333333336666'
    user_status_esperado = 0
    status_code_esperado = 200  # comunicação

    headers = {'Content-Type': 'application/json'}

    # Executa

    resposta = requests.get(f'{url}/{username}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['username'] == username_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['phone'] == telefone_esperado
    assert corpo_da_resposta['userStatus'] == user_status_esperado



