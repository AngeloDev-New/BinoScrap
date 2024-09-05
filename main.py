import config as C
import analyzer as A
VENDA = 1
COMPRA = 2
XPATH_COMPRA = '//*[@id="qa_trading_dealUpButton"]/button/span/div'
XPATH_VENDA = '//*[@id="qa_trading_dealDownButton"]/button/span/div'
XPATH_CANVAS = '//*[@id="chart"]/canvas'

#import time
#C.BINOMO_USERNAME
#C.BINOMO_PASSWORD
import base64
import cv2
import numpy as np
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def GetCanvas(XPATH_ATUAL,driver):
    wait = WebDriverWait(driver, 10)
    image_field = wait.until(EC.presence_of_element_located((By.XPATH, PATH)))
    canvas_image_base64 = driver.execute_script("""
        var canvas = arguments[0];
        return canvas.toDataURL('image/png').split(',')[1];
    """, canvas)
    image_data = base64.b64decode(canvas_image_base64)
    image_array = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    is_success, buffer = cv2.imencode('.png', image)
    if not is_success:
        raise ValueError("Não foi possível codificar a imagem em PNG")
    return BytesIO(buffer)


driver = webdriver.Chrome()
driver.get("https://binomo.com/auth")
XPATH_ATUAL = '//*[@id="qa_auth_LoginEmailInput"]/way-input/div/div[1]/way-input-text/input'
EscrevaAqui(XPATH_ATUAL,driver,C.BINOMO_USERNAME)
XPATH_ATUAL = '//*[@id="qa_auth_LoginPasswordInput"]/way-input/div/div/way-input-password/input'
EscrevaAqui(XPATH_ATUAL,driver,C.BINOMO_PASSWORD)
XPATH_ATUAL = '//*[@id="qa_auth_LoginBtn"]/button'
CliqueAqui(XPATH_ATUAL,driver)



for ESCOLHA in A.analyzeImage(GetCanvas(XPATH_CANVAS,driver)):
    match ESCOLHA:
        case VENDA:
            CliqueAqui(XPATH_VENDA,driver)
            continue
        case COMPRA:
            CliqueAqui(XPATH_COMPRA,driver)
            continue

#time.sleep(30)
driver.close()






#CliqueAqui(XPATH_ATUAL,driver)
#EscrevaAqui(XPATH_ATUAL,driver,USER)