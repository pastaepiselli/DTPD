from typing import Self, Any
from StringType import Valuta

class RealGEZ(float):
    # Tipo di dato specializzato reale >=0
    def __new__(cls, v: float|int|str|bool|Self):
        n :float = super().__new__(cls, v) #prova a convertire v in float
        if n >=0:
            return n
        raise ValueError(f"Il valore {n} è negativo!")
    
    


class IntGEZ(int):
    def __new__(cls, value:int|float|str|bool|Self):
        n:int = super().__new__(cls,value)
        if n >=0:
            return n 
        raise ValueError(f"Il valore {n} è negativo")
    


class IntGZ(int): 
    def __new__(cls, value:int|str|Self)->int|str: 
        n:int = super().__new__(cls, value)
        if n>0:
            return n
        raise ValueError(f"Il valore {n} è negativo")


class Voto(int): 
    def __new__(cls, n:int|Self)->int|str:
        voto:int = super().__new__(n)
        
        if voto in range(0,n):
            return voto
        
        raise ValueError(f"Il valore {n} del voto non è compreso nel range")



class FloatDenaro(float): 
    valuta: Valuta
    def __new__(cls, imp: float, val: Valuta)->Self:
        d = super().__new__(cls, imp)
        d.valuta = val
        return d
    def importo(self)-> float:
        return self.real
    def valuta(self)->Valuta:
        return self._valuta
    def __str__(self):
        return f"{self.importo()} {self.valuta()}"
    def __repr__(self):
        return f"Denaro: {self.importo()} unità di valuta {self.valuta()}"
    
