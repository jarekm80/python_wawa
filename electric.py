class ElectricCar:
    def __init__(self) -> None:
        self.stopien_naladowania = 100
    def drive(self,odleglosc):
        if odleglosc<self.stopien_naladowania: self.stopien_naladowania-=odleglosc
        else:
            stop