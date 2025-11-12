from typing import Self, Any
from enum import *

import re

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
    
class CarPlate(str):
    __pattern_5 = re.compile(r"^(?:[A-Z]{2}\d{3}[A-Z]{2}|[A-Z]{1,2}\d{5,6}|[A-Z0-9]{1,3}[- ]?\d{1,4}[- ]?[A-Z0-9]{0,3})$")
    def __new__(cls, plate:str)->str:
        if not cls.__pattern_5.match(plate): 
            raise ValueError(f"Invalid value: {plate}")
        return super().__new__(cls, plate)

class HashTag(str): 
    __pattern_6 = re.compile(r"^#[A-Za-z0-9_]+$")
    def __new__(cls, hashTag:str)->str: 
        if not cls.__pattern_6.match(hashTag):
            raise ValueError(f"Invalid Value")
        return super().__new__(cls, hashTag)


class Provincia(str): 
    __pattern_7 = re.compile(r"^[A-Z]{2}$")
    
    def __new__(cls, prov:str)->Self:
        prov:str = prov.upper().strip()
        if not cls.__pattern_7.match(prov):
            raise ValueError("Invalid Value")
        return super().__new__(cls, prov)


class CodiceVolo(str):
	# Gli oggetti di questa classe *sono* stringhe
	#  che rispettano il formato dei codici dei voli: XY1234
	def __new__(cls, cv: str) -> Self:
		cv: str = cv.upper().strip() # rendo la stringa maiuscola e senza spazi iniziali e finali
		if re.fullmatch(r'^[A-Z0-9]{2}\d{4}$', cv):
			return super().__new__(cls, cv)
		
		raise ValueError(f"La stringa '{cv}' non è un codice valido per un volo!")

class CodiceIATA(str):
	def __new__(cls, c: str) -> Self:
		if re.fullmatch(r'^[A-Z]{3}$', c):
			return super().__new__(cls, c)
		
		raise ValueError(f"La stringa '{c}' non è un codice IATA valido per un aeroporto!")



