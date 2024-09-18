from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pywhatkit
import time
from datetime import datetime, date
from dotenv import load_dotenv
import os

listaSlide = ['White', 'Ultra Black', 'Mint']
listaGrafiato = []
listaLaufen = []

# Load environment variables from the .env file
load_dotenv()

# Now you can access the variables
email = os.getenv("EMAIL")
senha = os.getenv("SENHA")
grafiato = os.getenv("GRAFIATO")
laufen = os.getenv("LAUFEN")
slide = os.getenv("SLIDE")

#options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')

#variaveis
EMAILFIELD = (By.ID, "ELOGIN")
PASSWORDFIELD = (By.ID, "ESENHA")
BOTAOLOGIN = (By.CLASS_NAME, "col-xs-12")
COOKIES = (By.ID, "cn-accept-cookie")
BARRAPESQUISA = (By.ID, "EPESQUISA")
BOTAOPESQUISA = (By.ID, "BTNPESQUISA")


def main():
    browser = webdriver.Chrome(options=options,)
    browser.get('http://prontaentrega.diklatex.com.br/login')
    time.sleep(7)
    browser.refresh()
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(email)
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(senha)
    time.sleep(5)
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BOTAOLOGIN)).click()
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BARRAPESQUISA)).send_keys(slide)
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BOTAOPESQUISA)).click()
    
    

    # elements = WebDriverWait(browser, 10).until(
    #     EC.presence_of_all_elements_located(BOTAOLOGIN)
    # )
    # second_element = elements[3]
    # second_element.click()
    # browser.navigate().refresh()

    # # wait for email field and enter email
    # # Click Next
    # WebDriverWait(browser, 100).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    # # wait for password field and enter password
    # # Click Login - same id?
    # WebDriverWait(browser, 100).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    # #nao 
    # WebDriverWait(browser, 100).until(EC.element_to_be_clickable(NAO)).click()
    # #clicar no botão da matéria de macro
    # WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BOTAOMACRO)).click()
    # #clicar no botao de trabalho
    # WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BOTAOTRABALHO)).click()
    # #card trabalho
    # cardTabalho = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "sc-bbSZdi jMzIvF cardTrabalho")))
    # for o in cardTabalho:
    #     cardTabalho.click()
    #     print(o)
    

main()
