from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

os.system('cls')
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

time.sleep(1)
def LOGIN():
    usuario = 'JauumGOD'
    senha = 'A1h2q4v1@1'
    
    global navegador
    navegador.get("https://www.bet365.com/#/HO/")
    time.sleep(2)
    navegador.maximize_window()

    #usuario
    navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div[4]/div[3]/div').click()
    navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/input').click()
    navegador.find_element('xpath','/html/body/div[1]/div/div[3]/div/div[2]/input').send_keys(usuario)
    time.sleep(1)
    #password
    navegador.find_element('xpath','/html/body/div[1]/div/div[3]/div/div[3]/input').click()
    navegador.find_element('xpath','/html/body/div[1]/div/div[3]/div/div[3]/input').send_keys(senha)
    #login
    navegador.find_element(By.CLASS_NAME,'div.lms-LoginButton').click()
    navegador.maximize_window()


def ENCONTRAR_TELA():
    #select type service
    navegador.find_element('xpath','//*[@id="nav-Tickets"]/a').click()
    navegador.find_element('xpath','//*[@id="nav-Tickets-Statusview"]/a').click()
    navegador.find_element('xpath','//*[@id="TicketID_160395"]/td[7]/div').click()
    time.sleep(2)

def ANALISAR_JOGO():

    print('concluido')

def ENVIAR_MSG_ZAP():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    dados = navegador.find_element('xpath','/html/body/text()[2]').text()
    print(dados)
    




time.sleep(1)
navegador.close()