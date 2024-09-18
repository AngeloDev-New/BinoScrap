VENDA = 1
COMPRA = 2
INSTABILIDADE = 3
import random
import time

def analyze(lastCandles):
    while True:
        time.sleep(10)
        yield random.randint(1, 3)

    
    
