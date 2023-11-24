import requests

nome = 'EMPRESA BRASILEIRA DE CORREIOS E TELEGRAFOS'

url = ''
accesskey = ''
secretkey = ''
params = {
    'AccessKey': accesskey,
    'SecretKey': secretkey
}
nome = {
    'nome': f'{nome}'
}

contrato = requests.get(url)

print(contrato)