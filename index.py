# na hora que eu mandar o comando no wpp ele via rodar o programa e me dar informação que eu quero 

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pywhatkit
import time
from datetime import datetime, date



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
CARDTRABALHO = (By.XPATH, "//div[@class='sc-iRqkff bpukjd'][last()]//li//svg")
DATA = (By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/section[1]/article[1]/section[1]/div[1]/div[1]/header[1]/div[1]/div[2]/div[1]/div[3]")


# //button[@aria-label='Acessar Trabalho Lista de Exercícios - Cap 2']//i[@class='css-10ikh9f']//*[name()='svg'] -> o que dava certo para clicar no botao do card trabalho



def main():

    #functions
    browser = webdriver.Chrome(options=options,)
    browser.get('https://estudante.ibmec.br/disciplinas')
    #clicar no botão de logar no site do ibmec
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BOTAOIBMEC)).click()
    # wait for email field and enter email
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys("seu email")
    # Click Next
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    # wait for password field and enter password
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys("sua senha")
    # Click Login - same id?
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    #nao 
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(NAO)).click()
    #clicar no botão da matéria de macro
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BOTAOMACRO)).click()
    #clicar no botao de trabalho
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(BOTAOTRABALHO)).click()
    #card trabalho

    
       
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable(CARDTRABALHO)).click()
    elements = WebDriverWait(browser, 100).until(EC.presence_of_all_elements_located((By.XPATH, "//p[contains(text(),'Não é possível enviar um trabalho. O prazo se ence')]")))
    x = elements[0].text
    wordData = x.split()
    dataReal = wordData[-1]
    dataReal = dataReal[:-1]
    format = "%d/%m/%Y"
    dataa = datetime.strptime(dataReal, format)
    if datetime.date(dataa) == datetime.today().date():
        print(f'Hoje, {dataReal}, tem atividade para entregar')
    else:
        print('nao tem atividade para hoje')
        # WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.CLASS_NAME, "sc-cPiKLX czwAXI"))).click()
    
       #WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Acessar página inicial']//i[@class='css-10ikh9f']//*[name()='svg']"))).click()

    
main()



#css selector e for function
    

    
#print(dataReal)
    
# if __name__ == '__main__':
#     while True:
#         main()
#         time_wait = 1440
#         print(f'Waiting {time_wait} minuts...')
#         time.sleep(time_wait * 60)



