from typing import Self, Any
from enum import *
from datetime import date
import re
from NumericType import FloatDenaro
class CodiceFiscale(str):
    __pattern = re.compile(r"^[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}$")
    def __new__(cls, new_pattern:str)->Self:
        new_pattern = new_pattern.upper()
        # Controlla che new_pattern rispetti il pattern della variabile __pattern
        #Se ciò non accade solleva un errore
        if not cls.__pattern.match(new_pattern):
            raise ValueError(f"Il codice fiscale inserito non è valido: {new_pattern}")
        # Se il pattern è valido ritorna l'istanza come sottoclasse
        return super().__new__(cls, new_pattern)


class PartitaIva(str):
    __pattern_2 = re.compile(r"\d{11}+")
    def __new__(cls, iva:str):
        if not cls.__pattern_2.match(iva):
            raise ValueError (f"Valore non valido: {iva}")
        return super().__new__(cls, iva)


class CAP(str):
    def __new__(cls, cap:str) ->Self:
        if re.fullmatch(r'^\d{5}$', cap):
            return super().__new__(cls,cap)
        raise ValueError(f"La stringa '{cap}' non è un CAP italiano valido!")





class Valuta(str):
    def __new__(cls, v:str)->Self:
        if re.fullmatch(r'^[A-Z]{3}$', v):
            return super().__new__(cls, v)
        raise ValueError(f"La stringa'{v}' non è un codice valido per una valuta!")



def  add(self,other: Self) ->Self:
    """
    Somma self ad un'altra istanza di Denaro, ma solo se la valuta è la stessa.
    Restituisce una nuova istanza di Denaro
    """    
    if self.valuta() !=other.valuta():
        raise ValueError (f"Non posso sommare importi di valute diverse {self.valuta()} e {other.valuta()}")
    somma:float = self.importo() + other.importo()
    return Denaro(somma, self.valuta())

def __sub__(self, other:Self)->Self:
    return self + FloatDenaro(-other, other.valuta())

"""
Gli oggetti denaro li volgio usare come float qualsiasi
è il tipo di dato denaro basato sul float: essendo l'istanza di Denaro con la valuta eredita float e in più ha un campo valuta,
e in più 
"""

class Email(str):
    __pattern_3 = re.compile(r"[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}")
    def __new__(cls, mail:str):
        if not cls.__pattern_3.match(mail):
            raise ValueError (f"Valore non valido: {mail}")
        return super().__new__(cls, mail)



class Telefono(str):
    __patern_4 = re.compile(r"\+[0-9]{10}")
    def __new__(cls, phone:str):
        if not cls.__patern_4.match(phone):
            raise ValueError(f"Valore non valido: {phone}")
        return super().__new__(cls, phone)
    


class Targa(str):
    # __pattern_5: re.compile(r"")
    pass






