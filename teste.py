import json
import time
import requests
from bs4 import BeautifulSoup as bs

from urllib.parse import parse_qs, urlparse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#
# url = 'http://www.transparencia.go.gov.br/portaldatransparencia/gastos-governamentais/contratos'
# driver.get(url)
# driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/button[2]').click()
# driver.find_element(By.XPATH, '//*[@id="search--3"]/form/label/input').send_keys("augusto 0001")
#
# iframe = driver.find_element(By.XPATH, '//iframe[@id="blockrandom"]')
# driver.switch_to.frame(iframe)
# time.sleep(10)

# https://portaldatransparencia.gov.br/busca/pessoa-juridica/07669168000133
#  27338637
#  322817278

#----------------------------------------------------------------------------------------------------------------

# h = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
# req = requests.get('https://portaldatransparencia.gov.br/busca/pessoa-juridica/37152127000136', headers=h)
# req2 = bs(req.text, 'html.parser')
# id = req2.find('input', attrs={'id': 'skModulo'})
# v = id['value']
#
# print(v)
# print(id)
# print(req2)

#----------------------------------------------------------------------------------------------------------------

# cnpj = '36765378000123'
# cnpj = '07669168000133'
#
# url = f'https://transparencia.gov.br/busca/pessoa-juridica/{cnpj}'
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
#
# driver = webdriver.Chrome(options=chrome_options)
# wait = WebDriverWait(driver, timeout=10)
#
# driver.get(url)
# try:
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnAbaContratosFirmados"]'))).click()
#     fornecedor_url = str(
#         wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="url-contratos-firmados"]'))).get_attribute('href'))
# except:
#     contratos = []
#     print("oh shits here we go again")
#     exit(code=1)
#
# fornecedor_url = urlparse(fornecedor_url)
# fornecedor_id = parse_qs(fornecedor_url.query)['fornecedor']
#
# driver.quit()
#
# url = f'https://www.portaltransparencia.gov.br/contratos/consulta/resultado'
# params = {
#     'fornecedor': fornecedor_id,
#     'colunasSelecionadas': ' '
# }
#
# h = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
# list_size = requests.get(url, params, headers=h).json()['recordsTotal'] #????
#
# params = {
#     'tamanhoPagina': list_size + 1,
#     'fornecedor': fornecedor_id,
#     'colunasSelecionadas': ['linkDetalhamento', 'dataAssinatura', 'dataPublicacaoDOU', 'dataInicioVigencia',
#                             'dataFimVigencia', 'orgaoSuperior', 'orgaoEntidadeVinculada', 'unidadeGestora',
#                             'formaContratacao', 'grupoObjetoContratacao', 'numeroContrato', 'nomeFornecedor',
#                             'cpfCnpjFornecedor', 'situacao', 'valorContratado'],
# }
#
# contratos = requests.get(url, params).json()['data']
#
# print(list_size)
# print(contratos)

#-----------------------------------------------------
# [{'id': 86421448,
# 'dataAssinatura': '07/06/2021',00
# 'dataPublicacaoDOU': '09/06/2021',00
# 'dataInicioVigencia': '07/06/2021',00
# 'dataFimVigencia': '07/06/2026',00
# 'orgaoSuperior': 'MINISTERIO DO PLANEJAMENTO,DESENV. E GESTÃO',00
# 'orgaoEntidadeVinculada': 'MINISTERIO DO PLANEJAMENTO,DESENV. E GESTÃO',00
# 'unidadeGestora': 'FUND.DE PREVID.COMPL.SERV.PUB.FED.PODER EXEC.',00
# 'formaContratacao': 'Concorrência',00
# 'grupoObjetoContratacao': 'Outros',00
# 'numeroContrato': '3/2021',00
# 'processo': None,
# 'tipoFornecedor': 'pessoa-juridica',
# 'idFornecedor': '07669168000133',
# 'nomeFornecedor': 'INTECH SOLUCOES EM TECNOLOGIA DA INFORMACAO LTDA',
# 'cpfCnpjFornecedor': '07.669.168/0001-33',
# 'ufFornecedor': None,
# 'municipioFornecedor': None,
# 'situacao': 'Não se aplica',
# 'objeto': None,
# 'valorContratado': '12.163.350,00'},

# linkDetalhamento', 'dataAssinatura'00, 'dataPublicacaoDOU'00, 'dataInicioVigencia'00,
# 'dataFimVigencia'00, 'orgaoSuperior'00, 'orgaoEntidadeVinculada'00, 'unidadeGestora'00,
# 'formaContratacao'00, 'grupoObjetoContratacao'00, 'numeroContrato'00, 'nomeFornecedor',
# 'cpfCnpjFornecedor', 'situacao', 'valorContratado

# Message: 'chromedriver-linux64' executable may have wrong permissions. Please see https://chromedriver.chromium.org/home

#-----------------------------------------------------
#
# cnpj = '07669168000133'
# url = f'https://transparencia.gov.br/busca/pessoa-juridica/{cnpj}'
# h = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
# dropdonw_site_html = requests.get(url, headers=h)
# site_html = bs(dropdonw_site_html.text, 'html.parser')
# # print(site_html)
# id = site_html.findAll('a', attrs={'class': 'box-ficha__botao'})
# for i in id:
#     try:
#         v = i['href']
#     except:
#         pass
#     print(i.text)
#     print(v)

# v = id['value']

#-----------------------------------------------------

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)
#
# cnpj = '07669168000133'
# url = f'https://portaldatransparencia.gov.br/criterios/pessoa/autocomplete?q={cnpj}'
# h = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
# dropdonw_site_html = requests.get(url, headers=h)
# site = bs(dropdonw_site_html.text, 'html.parser')
# pre_site3 = str(site).split('"')
# site3 = json.loads(pre_site3[3])
# print(site3)
#
# url = f'https://portaldatransparencia.gov.br/criterios/contratos/fornecedor/autocomplete?q={cnpj}'
# h = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
# dropdonw_site_html = requests.get(url, headers=h)
# site = bs(dropdonw_site_html.text, 'html.parser')
# pre_site3 = str(site).split('"')
# site3 = json.loads(pre_site3[3])
# print(site3)

#-----------------------------------------------------

# url = f'https://portaldatransparencia.gov.br/contratos/consulta/resultado?fornecedor=139100024&tamanhoPagina=999&colunasSelecionadas=linkDetalhamento,%20dataAssinatura,%20dataPublicaaoDOU,%20dataInicioVigencia,%20dataFimVigencia,%20orgaoSuperior,%20orgaoEntidadeVinculada,%20unidadeGestora,%20formaContratacao,%20grupoObjetoContratacao,%20numeroContrato,%20nomeFornecedor,%20cpfCnpjFornecedor,%20situacao,%20valorContratado'
# h = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
#
# req = requests.get(url, headers=h)
# print(req)
# print(req.text)
#
# print(type(req))
#
# driver.get(url)
# content = driver.find_element(By.TAG_NAME, 'pre').text
# print(content)
#
# {"draw":0,"recordsTotal":7,"recordsFiltered":7,"data":[{"id":97825187,"dataAssinatura":"01/02/2022",
# "dataPublicacaoDOU":"","dataInicioVigencia":"01/02/2022","dataFimVigencia":"20/06/2024",
# "orgaoSuperior":"Ministério da Educação","orgaoEntidadeVinculada":"Instituto Federal do Amazonas",
# "unidadeGestora":"IFAM - CAMPUS MANAUS CENTRO","formaContratacao":"Tomada de Preços",
# "grupoObjetoContratacao":"Outros","numeroContrato":"17/2021","processo":null,"tipoFornecedor":"pessoa-juridica",
# "idFornecedor":"34222656000170","nomeFornecedor":"JWL CONSTRUCOES DE EDIFICIOS LTDA",
# "cpfCnpjFornecedor":"34.222.656/0001-70","ufFornecedor":null,
# "municipioFornecedor":null,"situacao":"Não se aplica","objeto":null,
# "valorContratado":"2.057.489,05"},{"id":102625891,"dataAssinatura":"24/07/2023","dataPublicacaoDOU":"",
# "dataInicioVigencia":"24/07/2023","dataFimVigencia":"04/05/2024","orgaoSuperior":"Ministério da Educação",
# "orgaoEntidadeVinculada":"Instituto Federal do Amazonas",
# "unidadeGestora":"IFAM - CAMPUS PRESIDENTE FIGUEIREDO","formaContratacao":"Tomada de Preços",
# "grupoObjetoContratacao":"Outros","numeroContrato":"16/2023","processo":null,"tipoFornecedor":"pessoa-juridica",
# "idFornecedor":"34222656000170","nomeFornecedor":"JWL CONSTRUCOES DE EDIFICIOS LTDA",
# "cpfCnpjFornecedor":"34.222.656/0001-70","ufFornecedor":null,"municipioFornecedor":null,"situacao":"Não se aplica",
# "objeto":null,"valorContratado":"549.620,37"},{"id":102625654,"dataAssinatura":"15/12/2021","dataPublicacaoDOU":"",
# "dataInicioVigencia":"15/12/2021","dataFimVigencia":"15/12/2023","orgaoSuperior":"Ministério da Educação",
# "orgaoEntidadeVinculada":"Instituto Federal do Amazonas","unidadeGestora":"IFAM - CAMPUS MANAUS ZONA LESTE",
# "formaContratacao":"Pregão","grupoObjetoContratacao":"Outros","numeroContrato":"8/2021","processo":null,
# "tipoFornecedor":"pessoa-juridica","idFornecedor":"34222656000170","nomeFornecedor":"JWL CONSTRUCOES DE EDIFICIOS LTDA",
# "cpfCnpjFornecedor":"34.222.656/0001-70","ufFornecedor":null,"municipioFornecedor":null,"situacao":"Não se aplica",
# "objeto":null,"valorContratado":"384.498,69"},{"id":97125060,"dataAssinatura":"22/09/2022","dataPublicacaoDOU":"",
# "dataInicioVigencia":"22/09/2022","dataFimVigencia":"21/04/2023","orgaoSuperior":"Ministério do Trabalho",
# "orgaoEntidadeVinculada":"Instituto Nacional do Seguro Social",
# "unidadeGestora":"SUPERINTENDENCIA REGIONAL NORTE/CENTRO-OESTE","formaContratacao":"Tomada de Preços",
# "grupoObjetoContratacao":"Outros","numeroContrato":"66/2022","processo":null,"tipoFornecedor":"pessoa-juridica",
# "idFornecedor":"34222656000170","nomeFornecedor":"JWL CONSTRUCOES DE EDIFICIOS LTDA",
# "cpfCnpjFornecedor":"34.222.656/0001-70","ufFornecedor":null,"municipioFornecedor":null,
# "situacao":"Não se aplica","objeto":null,"valorContratado":"213.500,11"},{"id":107126651,"dataAssinatura":"03/11/2020",
# "dataPublicacaoDOU":"","dataInicioVigencia":"03/11/2020","dataFimVigencia":"15/07/2021",
# "orgaoSuperior":"Ministério da Educação","orgaoEntidadeVinculada":"Fundação Universidade do Amazonas",
# "unidadeGestora":"FUNDACAO UNIVERSIDADE DO AMAZONAS","formaContratacao":"Sem Informação",
# "grupoObjetoContratacao":"Outros","numeroContrato":"24/2020","processo":null,"tipoFornecedor":"pessoa-juridica",
# "idFornecedor":"34222656000170","nomeFornecedor":"JWL CONSTRUCOES DE EDIFICIOS LTDA",
# "cpfCnpjFornecedor":"34.222.656/0001-70","ufFornecedor":null,"municipioFornecedor":null,
# "situacao":"Não se aplica","objeto":null,"valorContratado":"166.566,52"},{"id":92225274,
# "dataAssinatura":"25/11/2021","dataPublicacaoDOU":"","dataInicioVigencia":"25/11/2021",
# "dataFimVigencia":"24/04/2022","orgaoSuperior":"Ministério da Defesa","orgaoEntidadeVinculada":"Comando da Aeronáutica",
# "unidadeGestora":"GRUPAMENTO DE APOIO DE MANAUS","formaContratacao":"Pregão","grupoObjetoContratacao":"Outros",
# "numeroContrato":"39/2021","processo":null,"tipoFornecedor":"pessoa-juridica","idFornecedor":"34222656000170",
# "nomeFornecedor":"JWL CONSTRUCOES DE EDIFICIOS LTDA","cpfCnpjFornecedor":"34.222.656/0001-70","ufFornecedor":null,
# "municipioFornecedor":null,"situacao":"Não se aplica","objeto":null,"valorContratado":"47.749,00"},
# {"id":109025245,"dataAssinatura":"12/01/2022","dataPublicacaoDOU":"","dataInicioVigencia":"12/01/2022",
# "dataFimVigencia":"13/06/2022","orgaoSuperior":"Ministério da Defesa","orgaoEntidadeVinculada":"Comando da Aeronáutica",
# "unidadeGestora":"GRUPAMENTO DE APOIO DE MANAUS","formaContratacao":"Pregão","grupoObjetoContratacao":"Outros",
# "numeroContrato":"4/2022","processo":null,"tipoFornecedor":"pessoa-juridica","idFornecedor":"34222656000170",
# "nomeFornecedor":"JWL CONSTRUCOES DE EDIFICIOS LTDA","cpfCnpjFornecedor":"34.222.656/0001-70","ufFornecedor":null,
# "municipioFornecedor":null,"situacao":"Não se aplica","objeto":null,"valorContratado":"32.989,01"}],"error":null}

#-----------------------------------------------------


