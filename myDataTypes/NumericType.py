from typing import Self, Any
from StringType import Valuta

class RealGEZ(float):
    # Tipo di dato specializzato reale >=0
    def __new__(cls, v: float|int|str|bool|Self):
        n :float = super().__new__(cls, v) #prova a convertire v in float
        if n >=0:
            return n
        raise ValueError(f"Il valore {n} è negativo!")


# Tipo di dato specializzato: Intero >=0
class IntGEZ(int):
    def __new__(cls, value:int|float|str|bool|Self):
        n:int = super().__new__(cls,value)
        # Controlla che n sia maggiore o uguale a 0
        if n >=0:
            return n 
        
        # In caso contrario solleva un errore
        raise ValueError(f"Il valore {n} è negativo")


# Tipo di dato specializzato: Intero >0
class IntGZ(int): 
    def __new__(cls, value:int|str|Self)->int|str: 
        n:int = super().__new__(cls, value)
        
        # Controlla che n sia maggiore di 0
        if n>0:
            return n
        
        # In caso contrario solleva un errore
        raise ValueError(f"Il valore {n} è negativo")
    

class IntGE1900(int):
	# Tipo di dato specializzato Intero >= 1900
	def __new__(cls, v: float|int|str|bool|Self) -> Self:
		n: int = super().__new__(cls, v) # prova a convertire v in un int

		if n >= 1900:
			return n

		raise ValueError(f"Il valore {n} è minore di 1900!")

class Voto(int): 
    def __new__(cls, n:int|Self)->int|str:
        voto:int = super().__new__(n)
        
        # Controlla che voto sia compreso nel range a 0 n incluso  
        if voto in range(0,n+1):
            return voto
        
        # In caso contrario solleva un errore
        raise ValueError(f"Il valore {n} del voto non è compreso nel range")


