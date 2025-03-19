import json
def getItens(jsonPath):
    with open(jsonPath,'r') as itens:
        return json.load(itens)
    
def itensIterator(windownSize = 40,
                  windownOverlap = 1,
                  jsonPath = './convs/itens.json'):
    itens = getItens(jsonPath)
    for i in range(len(itens)):
        if i+windownSize>len(itens)-1:
            return
        yield itens[i:i+windownSize,windownOverlap]
        