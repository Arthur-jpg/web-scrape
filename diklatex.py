from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import Select
import pywhatkit


# Listas de cores e elementos
listaSlide = ['White', 'Ultra Black', 'Mint']
listaGrafiato = ['Branco', 'Ultra Black', 'Madrugada']
listaLaufen = ['Branco', 'Marinho Max']

listaMensagem = []
listaMensagens = []

# Carregar variáveis de ambiente
load_dotenv()

email = os.getenv("EMAIL")
senha = os.getenv("SENHA")
slide = os.getenv("SLIDE")
grafiato = os.getenv("GRAFIATO")
laufen = os.getenv("LAUFEN")
grupoid = os.getenv("CODGRUPO")

# Configurações do WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')

# Variáveis de elementos HTML
EMAILFIELD = (By.ID, "ELOGIN")
PASSWORDFIELD = (By.ID, "ESENHA")
BOTAOLOGIN = (By.CLASS_NAME, "col-xs-12")
BARRAPESQUISA = (By.ID, "EPESQUISA")
BOTAOPESQUISA = (By.ID, "BTNPESQUISA")
COR = (By.CLASS_NAME, "tag.col-3.col-sm-4.col-md-3.col-lg-5.text-truncate")
QUANTIDADEKG = (By.CLASS_NAME, "bottom-wrap")
FILTRO = (By.XPATH, "/html[1]/body[1]/div[3]/section[1]/div[1]/div[1]/div[4]/header[1]/div[1]/select[1]/option[3]")



def login(browser):
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(email)
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(senha)
    time.sleep(5)
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BOTAOLOGIN)).click()

def pesquisar(browser, tecido):
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BARRAPESQUISA)).send_keys(tecido)
    time.sleep(5) 
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BOTAOPESQUISA)).click()
    time.sleep(30) 


def filtro(browser):
    #Filtro de mais opção
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(FILTRO)).click()
    select_element = browser.find_element(By.XPATH, '/html[1]/body[1]/div[3]/section[1]/div[1]/div[1]/div[4]/header[1]/div[1]/select[1]')
    seletor = Select(select_element)
    seletor.select_by_index(len(seletor.options) - 1)
    time.sleep(30) 

def mandarParaLista(tecido, item, texto_quantidade):
    variavel = [tecido, item, texto_quantidade]
    listaMensagem.append(variavel)

def mensagemTexto():
    x = len(listaMensagem) - 1
    y = f'*{listaMensagem[x][0]}* na cor *{listaMensagem[x][1]}* possui *{listaMensagem[x][2]}* disponíveis \n'
    listaMensagens.append(y)

def printarMensagem():
    result = ''.join(map(str, listaMensagens))
    print(result)



def mandarMensagem():
    result = ''.join(map(str, listaMensagens))
    pywhatkit.sendwhatmsg_to_group_instantly(grupoid, result)

def acharInformacoes(browser, tecido, lista):
    elementos = browser.find_elements(*COR)
    encontrou = False
    for elemento in elementos:
        texto_elemento = elemento.text
        for item in lista:
            if item.lower() in texto_elemento.lower():
                encontrou = True
                # print(f"A opção '{item}' foi encontrada na página para o tecido {tecido}.")
                try:
                    quantidade = elemento.find_element(By.XPATH, './ancestor::figure//div[2]//span//small//b')
                    texto_quantidade = quantidade.text
                    mandarParaLista(tecido, item, texto_quantidade)
                    mensagemTexto()
                    # print('-'*30)
                    
                except:
                    texto_quantidade = 'não foram encontradas quantidades disponíveis'
                    print('-'*30)    


    if not encontrou:
        print("Nenhuma das opções foi encontrada.")
        print('-'*30)





def main():
    browser = webdriver.Chrome(options=options)
    browser.get('http://prontaentrega.diklatex.com.br/login')
    time.sleep(3)
    browser.refresh()

    #login
    login(browser)

    #slide
    pesquisar(browser, slide)
    filtro(browser)
    acharInformacoes(browser, slide, listaSlide)
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BARRAPESQUISA)).clear()

    #grafiato
    pesquisar(browser, grafiato)
    filtro(browser)
    acharInformacoes(browser, grafiato, listaGrafiato)
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BARRAPESQUISA)).clear()

    #laufen
    pesquisar(browser, laufen)
    filtro(browser)
    acharInformacoes(browser, laufen, listaLaufen)

    # printarMensagem()
    mandarMensagem()

    browser.quit()

main()
