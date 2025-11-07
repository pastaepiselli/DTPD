import re
from StringType import CAP, Valuta
class Indirizzo:
    _via: str 
    _civico: int 
    __cap_pattern:CAP
    def __init__(self, via: str, civico: int, cap: CAP) -> None:
        if not self.__cap_pattern.match(cap):
            raise ValueError (f"Il CAP fornito non è valido: {cap}")
        self._via = via
        self._civico = civico
        self._cap = cap
    def via(self) -> str:
        return self._via
    def civico(self) -> int:
        return self._civico
    def cap(self)-> str:
        return self._cap
    def __hash__(self) -> int:
        return hash((self._via, self._civico))
    def __eq__(self, other: Any) -> bool:
        if other is None or \
        not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        return self._via == other._via and self._civico == other._civico and self._cap == other._cap



class Denaro:
    """
    Rappresenta il tipo di dato concettuale composto
    con i seguenti campi:
        - importo: Reale
        - valuta: Valuta
    """  
    _importo: float
    _valuta: float
    def __init__(self, imp: float, val:Valuta):
        self._importo = imp
        self._valuta = val
        def importo(self) -> float:
            return self._importo
        def valuta(self)->Valuta:
            return self._valuta
        def __str__(self)-> str:
            return f"{self.importo()} {self.valuta()}"
        def __repr__(self) ->str:
            return f"Denaro: {self.importo()} unità di valuta {self.valuta()}"
        def __hash__(self)-> int:
            return hash((self.importo(), self.valuta()))
        def __eq__(self, other: Any) ->bool:
            if not isinstance(other, type(self)) or \
                hash(self) == hash(other):
                return False
            return self.importo() == other.importo() and \
            self.valuta() == other.valuta()
