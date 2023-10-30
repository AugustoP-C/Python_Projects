import requests
from bs4 import BeautifulSoup as bs

def scrape_nome(ni):
    h = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    url = f'https://portaldatransparencia.gov.br/busca/pessoa-juridica/{ni}'
    site = requests.get(url, headers=h)
    site_html = bs(site.text, 'html.parser')

    nome_formatado = ''
    nome = site_html.select(".dados-tabelados > div:nth-child(3) > div:nth-child(1) > span:nth-child(2)")
    for i in nome:
        nome_formatado = i.text

    return nome_formatado


#https://www.portaltransparencia.gov.br/busca/pessoa-juridica/37152127000136
#
# print(scrape_nome("34028316000707")) #76417005000186
# print(scrape_nome("76417005000186"))
