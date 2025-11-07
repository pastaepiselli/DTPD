from datetime import date

class IntDate(date):
    def __new__(cls, year, month, day):
        y:date = super().__new__(cls,year, month, day)
        if y.year > 1900:
            return y.year
        raise ValueError(f"L'anno {y.year} è minore o uguale 1900")

