# 1 - importação de pacotes

import json

# 2 - classes



# 3 - definições ( funções e metodos)

dados = {}


dados['cliente'] = [] # indica a criação de uma matriz lista
dados ['clientes'].append({
    'nome': 'Ana',
    'telefone':'519999999999',
    'email':'ana@teste.com.br'
})

with open('cliente.json', 'W') as outfile:
    json.dump(dados,outfile)