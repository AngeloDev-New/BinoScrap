from framework import *



#######################################_LOGANDO NA BINOMO_############################################
driver = webdriver.Chrome()                                                                         ##
driver.get("https://binomo.com/auth")                                                               ##
XPATH_ATUAL = '//*[@id="qa_auth_LoginEmailInput"]/way-input/div/div[1]/way-input-text/input'        ##
EscrevaAqui(XPATH_ATUAL,driver,BINOMO_USERNAME)                                                     ##
XPATH_ATUAL = '//*[@id="qa_auth_LoginPasswordInput"]/way-input/div/div/way-input-password/input'    ##
EscrevaAqui(XPATH_ATUAL,driver,BINOMO_PASSWORD)                                                     ##
XPATH_ATUAL = '//*[@id="qa_auth_LoginBtn"]/button'                                                  ##
CliqueAqui(XPATH_ATUAL,driver)                                                                      ##
######################################################################################################

try:
    for ESCOLHA in analyze(getCandles(100)):
        match ESCOLHA:
            case VENDA:
                CliqueAqui(XPATH_VENDA,driver)
                continue
            case COMPRA:
                CliqueAqui(XPATH_COMPRA,driver)
                continue
            case INSTABILIDADE:
                continue
finally:

#time.sleep(30)
    driver.close()






#CliqueAqui(XPATH_ATUAL,driver)
#EscrevaAqui(XPATH_ATUAL,driver,USER)'''
