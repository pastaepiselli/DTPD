from enum import *

class StatoOrdine(StrEnum):
    in_preparazione = auto()
    inviato = auto()
    da_saldare = auto()
    saldato = auto()