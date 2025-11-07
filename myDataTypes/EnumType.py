from enum import StrEnum, auto

class StatoOrdine(StrEnum):
    in_preparazione = auto()
    inviato = auto()
    da_saldare = auto()
    saldato = auto()

class Genere(StrEnum):
    donna = auto()
    uomo = auto()