VENDA = 1
COMPRA = 2
INSTABILIDADE = 3
import random
import time
import json
from padrao import *
def analyze(lastCandles,standards_size,ponderansa):
    objAnalista = ObjAnalista(
        lastCandles,
        standards_size,
        ponderansa
    )
    while objAnalista.online():
        yield objAnalista.Analize()
    objAnalista.saveMemory()



class ObjAnalista:
    def __init__(self,lastCandles,standards_size,ponderansa):
        self.lastCandles = lastCandles
        self.standards_size = standards_size
        self.ponderansa = ponderansa
        self.getOldPadroes()
        self.addActuallyPadroes()


    def Analize(self):
        pass
    
    def addActuallyPadroes(self):
        for padrao in getActuallyPadroes:
            self.padroes.append(padrao)


    def.getActuallyPadroes(self):









    def getOldPadroes(self):
        try:
            with open("standards.json","r") as json_file:
                self.padroes = json.loads(json_file)
        except:
            print("Memoria Zerada")
            self.padroes = []
        
    def saveMemory(self):
        indenT = len(self.padrao)
        standards = json.dumps(self.padroes,indent = indenT)
        with open("standards.json","w") as json_file:
            json_file.write(standards)

    def online(self):
        return self.lastCandles.active
    

