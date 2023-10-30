import time
from datetime import datetime
from selenium import webdriver
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import scrape_nome

wait = 60
driver = webdriver.Chrome()

cnpj = "47487870000109"

# cnpj = scrape_nome(cnpj1)

# obtetdo o numero total de paginas
url = f'https://cearatransparente.ce.gov.br/portal-da-transparencia/contratos/contratos?cod_concedente=+&cod_gestora=+&data_assinatura=&data_vigencia=&decricao_modalidade=+&descricao_situacaxdatalist-search_datalist=&locale=pt-BR&page=1000000&search={cnpj}&search_datalist=&search_sacc=&sort_column=integration_contracts_contracts.descricao_nome_credor&sort_direction=asc&tipo_objeto=+&__=__'

#Entrado no saite e esperando ele carregar, e pegando o total de paginas
driver.get(url)
time.sleep(15)
# WebDriverWait(nav, timee).until(EC.visibility_of_element_located(())).click()
# dropdown_total_pages = driver.find_element(By.XPATH, '/html/body/div[5]/div[6]/div/div/div[2]/div/div[2]/div/div[2]/div[5]/div').text
# dropdown_total_pages = WebDriverWait(driver, wait).until(EC.visibility_of_element_located(By.XPATH, '/html/body/div[5]/div[6]/div/div/div[2]/div/div[2]/div/div[2]/div[5]/div')).text
# total_pages = dropdown_total_pages.split("\n")
# pages = total_pages[len(total_pages) - 1]
pages = 1

links = []
for page in range(int(pages)):
    driver.get("https://cearatransparente.ce.gov.br/portal-da-transparencia/contratos/contratos?cod_concedente=+&cod_gestora=+&data_assinatura=&data_vigencia=&decricao_modalidade=+&descricao_situacaxdatalist-search_datalist=&locale=pt-BR&page=" + str(page + 1) + "&search=" + str(cnpj) + "&search_datalist=&search_sacc=&sort_column=integration_contracts_contracts.descricao_nome_credor&sort_direction=asc&tipo_objeto=+&__=__")
    time.sleep(10)
    dropdown_contratos = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[6]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/table/tbody')))
    contratos = dropdown_contratos.find_elements(By.TAG_NAME, 'tr')
    for dropdown_dados in contratos:
        dropdown_a = dropdown_dados.find_element(By.TAG_NAME, 'td')
        a = dropdown_a.find_element(By.TAG_NAME, 'a')
        link = a.get_attribute('href')
        links.append(link)
for dados in links:
    driver.get(dados)
    time.sleep(1)
    dropdown_numero = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[1]/h2').text
    dropdown_cnpj = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[2]/div[3]/div/p[2]').text
    data_inicio_vigencia = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[4]/div[2]/div/p[2]').text
    data_termino_vigencia = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[4]/div[3]/div/p[2]').text
    dropdown_valor_inicial = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[5]/div[5]/div/p[2]').text
    orgao = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[3]/div[1]/div/p[2]').text
    nome_fornecedor = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[2]/div[2]/div/p[2]').text


print(dropdown_numero)
print(dropdown_cnpj)
print(data_inicio_vigencia)
print(data_termino_vigencia)
print(dropdown_valor_inicial)
print(orgao)
print(nome_fornecedor)