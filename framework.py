VENDA = 1
COMPRA = 2
INSTABILIDADE = 3
XPATH_COMPRA = '//*[@id="qa_trading_dealUpButton"]/button/span/div'
XPATH_VENDA = '//*[@id="qa_trading_dealDownButton"]/button/span/div'






from getCan import *
import time
#BINOMO_USERNAME
#BINOMO_PASSWORD
from binApiLinkGen import *
from analyzer import *
from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import threading
def CliqueAqui(PATH,driver):
    wait = WebDriverWait(driver, 30)
    if ">" in PATH:
        search_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, PATH)))
    else:
        search_button = wait.until(EC.presence_of_element_located((By.XPATH, PATH)))
    search_button.click()

def EscrevaAqui(PATH,driver,texto):
    wait = WebDriverWait(driver, 10)
    input_field = wait.until(EC.presence_of_element_located((By.XPATH, PATH)))
    input_field.send_keys(texto)

def getJson(link):
    driver = webdriver.Chrome() 
    driver.get(link)
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'cm-content cm-lineWrapping')))
    json = element.get_attribute('textContent')
    driver.quit()
    return json

import urllib.request
import json
from urllib.request import urlopen

class getCandles(threading.Thread):
    def __init__(self,Numero):
        threading.Thread.__init__(self)
        self.qtdCandles = Numero
        self.getCandles()
        self.start()

    def run(self):
        while True:
            candle = next(self.lastCandles(1)) 
            if candle != self.candles[-1]:
                self.candles.append(candle)
                self.candles.pop(0)

    def getCandles(self):
        self.candles = []
        for candle in self.lastCandles(self.qtdCandles):
            self.candles.append(candle)


    def lastCandles(self,qtd):
        candlesBrute = []
        contador = 1
    

        while len(candlesBrute)<qtd:
            url = getLinkApi(contador)
            candlesBrute = getCandlesBrute(url)+candlesBrute
            contador+=1

        for candle in candlesBrute[qtd*-1:]:
            yield candle
if __name__ == "__main__":
    print(getJson('https://api.binomo.com/candles/v1/Z-CRY%2FIDX/2024-09-08T13:00:00/5?locale=br'))

    