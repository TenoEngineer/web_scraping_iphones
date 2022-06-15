from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date

today = date.today()


def scroll_down(driver):    #SCRIPT PARA DESCER ATÉ O FINAL DA PÁGINA
    driver = driver
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        time.sleep(SCROLL_PAUSE_TIME)
        time.sleep(SCROLL_PAUSE_TIME)
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def render_page(url):   #SCRIPT PARA GERAR HTML CORRETO PARA BS4
    driver = webdriver.Firefox()
    driver.get(url)
    scroll_down(driver)
    time.sleep(3)
    r = driver.page_source
    driver.quit()
    return r


def render_page_button(url):    #SCRIPT PARA GERAR HTML CORRETO PARA BS4 COM BOTÃO NO FINAL DA PÁGINA
    driver = webdriver.Firefox()
    driver.get(url)
    i = 0
    while i < 5:
        scroll_down(driver)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#__next > div.Loader__Wrapper-sc-1hj1bdl-0.fIAFvI > div > div > div.Row-sc-12954vt-0.pages__RowHasResults-sc-4fgpoh-1.bfPXnQ.hKbvrz > div.Grid-sc-8nmas1-0.bbwWpp > div > section > div.Row-sc-12954vt-0.fcqFeE > div > div > div > button'))).click()
        time.sleep(3)
        i+=1
    r = driver.page_source
    driver.quit()
    return r


def site_scroll_down(url) -> dict:  #PEGA DADOS COM PÁGINA QUE ATUALIZA DESCENDO A PÁGINA 
    r = render_page(url)
    bs = BeautifulSoup(r, 'lxml')
    box_product = bs.find_all('div',{'class': 'grid-box-descripion'})

    data = {"Competitor": [], "Title": [], "Price": [], "Date": []}

    for product in box_product:
        title = product.h3
        price = product.find('span',{'class': 'price-fraction'})

        if title is None or price is None:
            next
        elif int(price.text.strip().split(' ',)[1].split(',')[0].replace('.', '')) < int(2000):
            next
        else:
            data["Title"].append(title.text.strip())
            data["Price"].append(price.text.strip())
            data["Competitor"].append(url.split('.')[1])
            data['Date'].append(today.strftime("%d/%m/%Y"))
    
    return data


def per_page(url):  #PEGA DADOS COM PÁGINA COM PÁGINAS

    data = {"Competitor": [], "Title": [], "Price": [], "Date": []}

    i=0
    while i < 5:
        
        r = render_page(url)
        bs = BeautifulSoup(r, 'lxml')
        box_product = bs.find_all('a',{'aria-current': 'page'})
    
        for product in box_product:

            title = product.find('h3',{'class': 'product-name__Name-sc-1shovj0-0 gUjFDF'})
            price = product.find('span',{'class': 'price__PromotionalPrice-sc-h6xgft-1'})

            if title is None or price is None:
                next
            elif int(price.text.strip().split(' ',)[1].split(',')[0].replace('.', '')) < int(2000):
                next
            else:
                data["Title"].append(title.text.strip())
                data["Price"].append(price.text.strip())
                data["Competitor"].append(url.split('.')[1])
                data['Date'].append(today.strftime("%d/%m/%Y"))

        j = 24 * i
        i+=1
        page = 24 * i
        url = url.replace('offset='+str(j), 'offset='+str(page))

    return data


def same_company(url): #EXTRA, PONTO FRIO E CASAS BAHIA
    
    data = {"Competitor": [], "Title": [], "Price": [], "Date": []}

    r = render_page_button(url)
    bs = BeautifulSoup(r, 'lxml')
    box_product = bs.find_all('a',{'class': 'ProductCard__RedirectWrapper-sc-2vuvzo-3'})

    for product in box_product:
        title = product.find('h2',{'class': 'ProductCard__Title-sc-2vuvzo-0'})
        price = product.find('span',{'class': 'ProductPrice__PriceValue-sc-1tzw2we-6'})

        if title is None or price is None:
            next
        elif int(price.text.strip().split(' ',)[1].split(',')[0].replace('.', '')) < int(2000):
            next
        else:
            data["Title"].append(title.text.strip())
            data["Price"].append(price.text.strip())
            data["Competitor"].append(url.split('.')[1])
            data['Date'].append(today.strftime("%d/%m/%Y"))
    
    return data

def magalu (url):

    data = {"Competitor": [], "Title": [], "Price": [], "Date": []}

    i=1
    while i < 6:
        
        r = render_page(url)
        bs = BeautifulSoup(r, 'lxml')
        box_product = bs.find_all('div',{'data-testid': 'product-card-content'})

        for product in box_product:
            title = product.find('h2',{'data-testid': 'product-title'})
            price = product.find('p',{'data-testid': 'price-value'})
            if title is None or price is None:
                next
            elif int(str(price.text.strip()).split()[1].split(',')[0].replace('.', '')) < int(2000):
                next
            else:
                data["Title"].append(title.text.strip())
                data["Price"].append(price.text.strip())
                data["Competitor"].append(url.split('.')[1])
                data['Date'].append(today.strftime("%d/%m/%Y"))

        i+=1
        j = i - 1
        page = i
        url = url.replace('page='+str(j), 'page='+str(page))
    
    return data
