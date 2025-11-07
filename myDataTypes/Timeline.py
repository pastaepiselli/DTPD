


from datetime import datetime, date



class TimeRange(date): 
    def __new__(cls, year, month, day):
        return super().__new__(cls,year, month, day)

