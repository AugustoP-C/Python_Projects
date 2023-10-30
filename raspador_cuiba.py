import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import math
import scrape_nome

cnpj = '37152127000136'

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_prefs = {}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}

driver = webdriver.Chrome(options=chrome_options)  # 'module' object is not callable

driver.get('http://transparencia.cuiaba.mt.gov.br/portaltransparencia/transparencia/#/licitacao-contrato/contrato')
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="mat-input-6"]').send_keys(cnpj)
driver.find_element(By.XPATH, '//*[@id="cdk-accordion-child-0"]/div/form/div/button[1]').click()
time.sleep(5)

dropdown_n_page = driver.find_element(By.XPATH,
                                      '//*[@id="app-sub-menu"]/div/app-consult-grid/div/div/app-pagination/mat-paginator/div/div/div[2]/div').text
n_page = dropdown_n_page.split(' ')
dropdown_total_page = n_page[len(n_page) - 1]
total_page = math.ceil(int(dropdown_total_page) / 10)
print(total_page)
time.sleep(2)

for i in range(total_page):
    table = driver.find_element(By.XPATH, '//*[@id="app-sub-menu"]/div/app-consult-grid/div/div/app-grid/table')
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    list_tr = tbody.find_elements(By.TAG_NAME, 'tr')
    for tr in list_tr:
        list_td = tr.find_elements(By.TAG_NAME, 'td')
        del list_td[0]
        list_contrato = []
        for td in list_td:
            span = td.find_element(By.TAG_NAME, 'span').text
            list_contrato.append(span)

        print(list_contrato[0])
        print(cnpj)
        print(list_contrato[6])
        print(list_contrato[7])
        print(list_contrato[8])
        print(list_contrato[2])
        # print(scrape_nome(cnpj))

        contrato_dict = {
            'numero': list_contrato[0],
            'cnpj': cnpj,
            'data_inicio_vigencia': list_contrato[6],
            'data_fim_vigencia': list_contrato[7],
            'valor_inicial': list_contrato[8],
            'orgao': list_contrato[2],
            'fornecedor': scrape_nome(cnpj)
        }

# 37.152.127/0001-36 / 24.721.508/0001-47 / 03.372.237/0004-34
