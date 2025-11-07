class IntGez1900(int):
    def __new__(cls, year: int):
        if year >= 1900:
            return super().__new__(cls, year)
        return ValueError("Inserire un anno maggiore di 1900")