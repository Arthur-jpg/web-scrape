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


# Load environment variables from the .env file
load_dotenv()

# Now you can access the variables
email = os.getenv("EMAIL")
senha = os.getenv("SENHA")
db_password = os.getenv("DB_PASSWORD")



#options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')

#variaveis
EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")
NAO = (By.ID, "idBtn_Back")
BOTAOIBMEC = (By.XPATH, "//button[@aria-label='Entrar']")
BOTAOMACRO = (By.XPATH, "//section[@id='card-entrega-IBM3293']//footer[@class='sc-ifdsxC iPMzmn']")
BOTAOTRABALHO = (By.XPATH, "//button[@id='terceira-tab']")
CARDTRABALHO = (By.XPATH, "//button[@aria-label='Acessar Trabalho Lista de Exercícios - Cap 2']//i[@class='css-10ikh9f']//*[name()='svg']")
DATA = (By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/section[1]/article[1]/section[1]/div[1]/div[1]/header[1]/div[1]/div[2]/div[1]/div[3]")


def main():

    #functions
    browser = webdriver.Chrome(options=options,)
    browser.get('https://estudante.ibmec.br/disciplinas')
    #clicar no botão de logar no site do ibmec
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BOTAOIBMEC)).click()
    # wait for email field and enter email
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(email)
    # Click Next
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    # wait for password field and enter password
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(senha)
    # Click Login - same id?
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    #nao 
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(NAO)).click()
    #clicar no botão da matéria de macro
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BOTAOMACRO)).click()
    #clicar no botao de trabalho
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BOTAOTRABALHO)).click()
    #card trabalho
    cardTabalho = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "sc-bbSZdi jMzIvF cardTrabalho")))
    for o in cardTabalho:
        cardTabalho.click()
        print(o)
    

main()