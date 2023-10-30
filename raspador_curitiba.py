import requests
from unidecode import unidecode
from scrape_nome import scrape_nome

# <-<-<-ANOTAÇÕES IMPORTATES->->->
# imcopatbilidade de nosmes entre o portal da tranparencia e curitiba
# tipo do ato = 1 somente contratos


nome = 'EMPRESA BRASILEIRA DE CORREIOS E TELEGRAFOS'
# nome2 = 'PREFEITURA MUNICIPAL DE CURITIBA'

# nome2 = scrape_nome('10862298000100')
# nome = scrape_nome('34028316000707')
# print(nome2)
# nome_r = '7'
# https://cmcuritiba.eloweb.net/portaltransparencia-api/api/contratos?exercicio=2023&nome={n}&tipoAto=1
#
# url = f'https://cmcuritiba.eloweb.net/portaltransparencia-api/api/contratos?exercicio=2023&nome={nome2}&tipoAto=1'
#
# h = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
# req = requests.get(url, headers=h)
# f = req.text.split('{')
#
# print(f)
#
# del f[0]
# del f[0]
# del f[len(f) - 1]
#
# if len(f) != 0:
#     print('200(ok)')
#     dados = []
#     for i in f:
#         i = i.replace(':','').replace(',', '')
#         i = i.replace('[', '').replace(']', '').replace('}', '').replace('{', '')
#         dados = i.split('"')
#         for a in dados:
#             if a == '':
#                 x = dados.index(a)
#                 del dados[x]
#         for i in dados:
#             if i == 'descricaoEntidadeLicitacao':
#                 x = dados.index(i)
#                 orgao = dados[int(x) + 1]
#                 print(orgao)
#         #   descricaoEntidadeLicitacao
#         #   CÂMARA MUNICIPAL DE CURITIBA
#         print('-{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}-')
#         print(dados[9])
#         print('--------------------')
#         print(dados[11])
#         print('--------------------')
#         print(dados[13])
#         print('--------------------')
#         print(dados[15])
#         print('--------------------')
#         print(dados[17])
#         print('--------------------')
#         print(dados[19])
#         print('--------------------')
#         print(dados[7] + '/' + dados[3])
# else:
#     print('400')
#     exit(1)

n_contrato = ''
cnpj = ''
inicio_vigencia = ''
termino_vigencia = ''
valor = ''
orgao = ''

url = f'https://cmcuritiba.eloweb.net/portaltransparencia-api/api/contratos?exercicio=2023&nome={nome}&tipoAto=1'
h = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
req = requests.get(url, headers=h)
f = req.text.split('{')

del f[0]
del f[0]
del f[len(f) - 1]

if len(f) != 0:
    for i in f:
        i = i.replace(':', '').replace(',', '')
        i = i.replace('[', '').replace(']', '').replace('}', '').replace('{', '')
        dados = i.split('"')
        for a in dados:
            if a == '':
                x = dados.index(a)
                del dados[x]
        for d in dados:
            if d == 'displayContrato':
                n = dados.index(d)
                n_contrato = dados[int(n) + 1]
                # print(n_contrato)

            if d == 'cnpjCpf':
                n = dados.index(d)
                cnpj = dados[int(n) + 1]
                # print(cnpj)

            if d == 'inicioVigencia':
                n = dados.index(d)
                inicio_vigencia = dados[int(n) + 1]
                # print(inicio_vigencia)

            if d == 'terminoVigencia':
                n = dados.index(d)
                termino_vigencia = dados[int(n) + 1]
                # print(termino_vigencia)

            if d == 'valorContratado':
                n = dados.index(d)
                valor = dados[int(n) + 1]
                # print(valor)

            if d == 'descricaoEntidadeLicitacao':
                n = dados.index(d)
                orgao = dados[int(n) + 1]
                # print(orgao)

            contrato_dict = {
                'numero_contrato': n_contrato,
                'cnpj': cnpj,
                'data_inicio_vigencia': inicio_vigencia,
                'data_fim_vigencia': termino_vigencia,
                'valor_global': valor,
                'orgao': orgao,
            }
            print(contrato_dict)

else:
    print('400')