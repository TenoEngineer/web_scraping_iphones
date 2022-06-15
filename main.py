import pandas as pd
from functions import site_scroll_down, per_page, same_company, magalu
from manipulating import Manipulat
from excel import Excel


#LISTA DOS CONCORRENTES
fast_shop = 'https://www.fastshop.com.br/web/c/4611686018425427199/iphone;filters=price_BRL%253A%2528%257B1000%2B*%257D%2529'
americanas = 'https://www.americanas.com.br/busca/iphone?limit=24&offset=0' #O OFFSET VAI MUDANDO DE 24 EM 24 ATÉ O X14
casas_bahia = 'https://www.casasbahia.com.br/IPHONE/b' #Precisa clicar em botão
extra = 'https://www.extra.com.br/iphone/b' # Mesma estrutura das casas bahia
ponto_frio = 'https://www.pontofrio.com.br/iphone/b' #Mesma estrutura das casas bahia
magazine = 'https://www.magazineluiza.com.br/busca/iphone/?page=1'

sites = [fast_shop, americanas, casas_bahia, extra, ponto_frio, magazine]

feature_list = ["Competitor", "Title", "Price", "Date"]
base = pd.DataFrame(columns=feature_list)

#LOOP PARA CADA CONCORRENTE
for site in sites :
    
    if site == fast_shop:
       data = site_scroll_down(site)
       df = pd.DataFrame(data)

    if site == americanas:
       data = per_page(site)
       df = pd.DataFrame(data)

    if site == casas_bahia or site == extra or site == ponto_frio:
        data = same_company(site)
        df = pd.DataFrame(data)

    if site == magazine :
        data = magalu(site)
        df = pd.DataFrame(data)
        
    base = pd.concat([base,df])

base.to_csv("all_data.csv", sep=";", index=False)       #EXPORTA OS DADOS

list_gb = ['64', '128', '256', '512']
df = pd.read_csv('all_data.csv', delimiter=';', index_col=False)
Manipulat.finish(df)
Manipulat.increment_GB(list_gb, df)
Manipulat.export_csv(df)
Excel.paste_excel()