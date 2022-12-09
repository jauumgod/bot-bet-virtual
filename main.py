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
# site do bet
def LOGIN():
    usuario = 'user'
    senha = 'password'
    
    global navegador
    navegador.get("https://www.bet365.com/#/HO/")
    time.sleep(1)
    navegador.maximize_window()
    time.sleep(1)
    #usuario
    navegador.find_element('xpath','/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div[4]/div[3]/div').click()
    navegador.find_element('xpath','/html/body/div[1]/div/div[3]/div/div[2]/input').click()
    navegador.find_element('xpath','/html/body/div[1]/div/div[3]/div/div[2]/input').send_keys(usuario)
    time.sleep(1)
    #password
    navegador.find_element('xpath','/html/body/div[1]/div/div[3]/div/div[3]/input').click()
    navegador.find_element('xpath','/html/body/div[1]/div/div[3]/div/div[3]/input').send_keys(senha)
    #login
    navegador.find_element(By.CLASS_NAME,'div.lms-LoginButton').click()
    navegador.maximize_window()

def ENCONTRAR_TELA():
    pass

def ANALISAR_JOGO():
    pass

#whats login
def ENVIAR_MSG_ZAP():
    key = "Tulio"
    texto = "Opa saiu um novo resultado"
    msg = str(texto) + "Chance de win"
    servico = Service(ChromeDriverManager().install())
    whats = webdriver.Chrome(service=servico)
    whats.get('https://web.whatsapp.com/')
    time.sleep(1)
    whats.maximize_window()
    time.sleep(1)

    def localiza():
        #localizar chat
        whats.find_element('xpath','//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').click()
        whats.find_element('xpath','').send_keys(key)
        #enviar msg
        whats.find_element('xpath','//*[@id="pane-side"]/div[1]/div/div/div[6]/div/div/div/div[2]/div[1]/div[1]/span/span').click()
        whats.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').click()
        whats.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(msg)
        whats.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'). click()

    localiza()
    whats.close()

resultado = ANALISAR_JOGO()
 
while resultado ==True:
    time.sleep(60)
    ENVIAR_MSG_ZAP()


LOGIN()

time.sleep(1)
navegador.close()