import requests
from bs4 import BeautifulSoup
from lxml import etree
def all_products(product):
    list_titulos=[]
    list_precios=[]
    list_urls=[]
    siguiente="https://listado.mercadolibre.com.co/"+product
    while True:
        r=requests.get(siguiente)
        if r.status_code==200:
            soup=BeautifulSoup(r.content,"html.parser")
            #Titulos
            titulos=soup.find_all("h2",attrs={"class","ui-search-item__title"})
            titulos=[i.text for i in titulos]
            list_titulos.extend(titulos)
            #Precios
            dom=etree.HTML(str(soup))
            precios=dom.xpath('//li[@class="ui-search-layout__item"]//div[@class="ui-search-price ui-search-price--size-medium"]//div[@class="ui-search-price__second-line"]/span[@class="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript"]//span[@class="andes-money-amount__fraction"]')
            precios=[i.text for i in precios]
            list_precios.extend(precios)
            #Urls
            url=soup.find_all("a",attrs={"class","ui-search-item__group__element ui-search-link"})
            url=[link.get("href") for link in url]
            list_urls.extend(url)
            ini=int(soup.find("span", attrs={"class":"andes-pagination__link"}).text)
            cant=int(soup.find("li",attrs={"class":"andes-pagination__page-count"}).text.replace("de ",""))
        else:
            break
        print(ini,cant)
        if ini==cant:
            break
        siguiente=dom.xpath('//div[@class="ui-search-pagination"]/nav/li[contains(@class,"--next")]/a')[0].get("href")
    return  list_titulos,list_precios,list_urls  
def stop_product (product,limite):
    list_titulos=[]
    list_precios=[]
    list_urls=[]
    siguiente="https://listado.mercadolibre.com.co/"+product
    while True:
        r=requests.get(siguiente)
        if r.status_code==200:
            soup=BeautifulSoup(r.content,"html.parser")
            #Titulos
            titulos=soup.find_all("h2",attrs={"class","ui-search-item__title"})
            titulos=[i.text for i in titulos]
            list_titulos.extend(titulos)
            #Precios
            dom=etree.HTML(str(soup))
            precios=dom.xpath('//li[@class="ui-search-layout__item"]//div[@class="ui-search-price ui-search-price--size-medium"]//div[@class="ui-search-price__second-line"]/span[@class="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript"]//span[@class="andes-money-amount__fraction"]')
            precios=[i.text for i in precios]
            list_precios.extend(precios)
            #Urls
            url=soup.find_all("a",attrs={"class","ui-search-item__group__element ui-search-link"})
            url=[link.get("href") for link in url]
            list_urls.extend(url)
            ini=int(soup.find("span", attrs={"class":"andes-pagination__link"}).text)
            cant=int(soup.find("li",attrs={"class":"andes-pagination__page-count"}).text.replace("de ",""))
        else:
            break
        print(ini,cant)
        if len(list_titulos)>=int(limite):
           return  list_titulos[:limite],list_precios[:limite],list_urls[:limite] 
        if ini==cant:
            break
        siguiente=dom.xpath('//div[@class="ui-search-pagination"]/nav/li[contains(@class,"--next")]/a')[0].get("href")
    return  list_titulos,list_precios,list_urls  

