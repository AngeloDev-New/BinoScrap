# classe para armazenar padroes
class padrao:
    def __init__(self,padrao,ponderansa,fromCandle = False):
        if fromCandle:
            maior = max(padrao)
            menor = min(padrao)
            self.padrao = []
            for candle in padrao:
                self.padrao.append(((candle-menor)/(maior-menor))*100)
            else:
                self.ponderansa = ponderansa
                return

        self.padrao = padrao
        self.ponderansa = ponderansa

#recebe um outro padrao e retorna se o mesmo e similar ao primeiro
    def similar(self,Padrao)
        for index,pond in enumerate(self.ponderada):
            maxi = pond[1]
            minim = pond[0]
            candle = Padrao.padrao[index]
            if not (candle > minim and candle < maxi):
                return False
        return True
        
#retorna uma lista com maximo e minimo do padro para poder ser similar 
    def ponderada(self):
        pond = []
        for candle in self.padrao:
            minin = candle*(1-self.ponderansa)
            maxi = candle*(1+self.ponderansa)
            pond.append(minin,maxi)
        return pond
#retorna o espelho do padrao
    def mirror(self):
        mirror = []
        for candle in self.padrao:
            mirror.append(100-candle)
        return padrao(mirror,self.ponderansa) 
