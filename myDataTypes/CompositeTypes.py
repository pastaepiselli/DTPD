from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
	import re
	from StringType import CAP,Provincia
	from NumericType import IntGZ
	

class Indirizzo:
    _via: str 
    _civico: int 
    _cap:CAP
    def __init__(self, via: str, civico: int, cap: CAP) -> None:
        # questo dovrebbe dare errore perceh __cap_pattern non e definito e poi cap_pattenrn non ha .match()
        if not isinstance(cap, CAP):
            raise ValueError (f"Il CAP fornito non è valido: {cap}")
        self._via = via
        self._civico = civico
        self._cap = cap
        
    
    # Metodo getter per la via 
    def via(self) -> str:
        return self._via
    
    # Metodo getter per il civico
    def civico(self) -> int:
        return self._civico
    
    # Metodo getter per il cap 
    def cap(self)-> str:
        return self._cap
    
    # Metodo hash per i custom objects
    # Questo metodo confronta e ritorna un valore di hash degli oggetti (o attributi) passati che vengono di norma immagazzinati in un set o come chiavi di un dizionario
    def __hash__(self) -> int:
        return hash((self._via, self._civico))
    
    # Questo metodo confronta due oggetti per il loro valore 
    def __eq__(self, other: Any) -> bool:
        # Se other è None, o non è della stessa classe, o hanno il valore di hash diverso; ritorna false
        if other is None or \
        not isinstance(other, type(self)) or \
        hash(self) != hash(other):  #questo potrebbe generare collisioni tra oggetti con lo stesso hash(?)
            return False
        
        return self._via == other._via and self._civico == other._civico and self._cap == other._cap


