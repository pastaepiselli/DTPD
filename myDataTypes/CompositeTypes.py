import re
from StringType import CAP, Valuta

class Indirizzo:
    _via: str 
    _civico: int 
    __cap_pattern:CAP
    def __init__(self, via: str, civico: int, cap: CAP) -> None:
        # questo dovrebbe dare errore perceh __cap_pattern non e definito e poi cap_pattenrn non ha .match()
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
	# Rappresenta il tipo di dato concettuale composto
	#  con i seguenti campi:
	# 	- importo: Reale
	# 	- valuta: Valuta
	_importo: float
	_valuta: Valuta

	def __init__(self, imp: float, val: Valuta) -> None:
		self._importo = imp
		self._valuta = val

	def importo(self) -> float:
		return self._importo

	def valuta(self) -> Valuta:
		return self._valuta

	def __str__(self) -> str:
		return f"{self.importo()} {self.valuta()}"

	def __repr__(self) -> str:
		return f"Denaro: {self.importo()} unità di valuta {self.valuta()}"

	def __hash__(self) -> int:
		return hash( (self.importo(), self.valuta()) )

	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, type(self)) or \
			hash(self) != hash(other):
			return False
		return self.importo() == other.importo() and \
			self.valuta() == other.valuta()

	def __add__(self, other: Self) -> Self:
		"""
		Somma self ad un'altra istanza di Denaro,
		 ma solo se la valuta è la stessa.
		Restituisce una nuova istanza di Denaro
		"""
		if self.valuta() != other.valuta():
			raise ValueError(f"Non posso sommare importi di valute diverse: '{self.valuta()}' e '{other.valuta()}'")
		
		somma: float = self.importo() + other.importo()
		return Denaro(somma, self.valuta())

class FloatDenaro(float):
	_valuta: Valuta
	def __new__(cls, imp: float, val: Valuta) -> Self:
		d = super().__new__(cls, imp)
		
		d._valuta = val
		return d

	def importo(self) -> float:
		return self.real

	def valuta(self) -> Valuta:
		return self._valuta

	def __str__(self) -> str:
		return f"{self.importo()} {self.valuta()}"

	def __repr__(self) -> str:
		return f"Denaro: {self.importo()} unità di valuta {self.valuta()}"

	def __hash__(self) -> int:
		return hash( (self.importo(), self.valuta()) )

	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, type(self)) or \
			hash(self) != hash(other):
			return False
		return self.importo() == other.importo() and \
			self.valuta() == other.valuta()

	def __add__(self, other: Self) -> Self:
		"""
		Somma self ad un'altra istanza di Denaro,
		 ma solo se la valuta è la stessa.
		Restituisce una nuova istanza di Denaro
		"""
		if self.valuta() != other.valuta():
			raise ValueError(f"Non posso sommare importi di valute diverse: '{self.valuta()}' e '{other.valuta()}'")
		
		somma: float = self.importo() + other.importo()
		return FloatDenaro(somma, self.valuta())

	def __sub__(self, other: Self) -> Self:
		return self + FloatDenaro(-other, other.valuta())
