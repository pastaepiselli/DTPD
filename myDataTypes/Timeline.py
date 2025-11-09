from datetime import datetime, date

class TimeRange(date): 
    def __new__(cls, start: datetime, end: datetime):
        # non so che cosa ho scritto
        if end < start:
            return ValueError("Start date cant be higher than end date")
        return super().__new__(cls, start, end)
        

