from datetime import datetime
import re



class Days(list): 
    days:list[str]
    valid_days = ["Lunedi", "Martedi", "Mercoledi", "Giovedi", "Venerdi", "Sabato", "Domenica"]
    def __init__(self, days: list[str] = None):
        
        # Se days è None, viene assegnata una lista vuota, altrimenti viene assegnata la lista passata come argomento 
        days = [] if days is None else days #questa è una variabile locale; non dell'istanza self.days
        
        # Itero sugli elementi della lista valid_days
        for d in days:
            
            # Se i giorni non sono dentro la lista valid_days 
            if d not in Days.valid_days:
                # Solleva un errore
                raise ValueError(f"Giorno non valido: {d}")
        # Altrimenti inizializzo la lista ereditata da list()
        super().__init__(days)


# La classe datetime.date è una data non un intervallo; non ha senso ereditare da date 
class TimeRange: 
    start:datetime
    end:datetime
    days:Days #adesso days è un singolo oggetto di Days, non più una lista di stringhe 
    def __init__(self, start:datetime, end:datetime, days: list[str] = None):
        # Se il valore di endè minore di start
        if end<start: 
            # Solleva un errore
            raise ValueError("La data di fine non può precedere quella di inizio")
        # In caso contrario inizializza i due attributi
        self.start = start
        self.end = end 
        
        # Inizializzo un oggetto Days, anche vuoto se non viene passato come argomento 
        self.days = Days(days) 
        
    
    
    # Metodo per verificare se un istante è compreso nell'intervallo di tempo
    def contains(self, moment:datetime)-> bool: 
        return self.start <= moment <=self.end
    
    
    # Metodo che gestisce la durata totale delle ora del periodo di tempo
    def duration (self): 
        return self.end - self.start
    
    
    def __repr__(self):
        return f"TimeRange(start={self.start}, end={self.end}, days = {self.days})"
    
    def __str__(self):
        return f"Inizio: {self.start}.\nFine:{self.end}\nGiorni: {self.days}"
    

def main()->None:
    t1:TimeRange = TimeRange(start=datetime(2025, 11, 12, 9),
        end=datetime(2025, 11, 12, 17),
        days=["Lunedi", "Mercoledi"] 
    )
    
    print(t1)
    print(t1.contains(moment=datetime(2025,11,12,10)))
    print(t1.duration())

if __name__ == "__main__":
    main()