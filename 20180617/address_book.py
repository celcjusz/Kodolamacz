class Kontakt():
    def __init__(self, imie = "", nazwisko = "", adresy = []):
        self.imie = imie
        self.nazwisko =  nazwisko
        self.adresy = adresy
    def __str__(self):
        out = f'{self.imie} {self.nazwisko}'
        if len(self.adresy) > 0:
            return f'{out} {self.adresy}'
        else:
            return out
    def __repr__(self):
        # można odwołać się do  innej metody w klasie
        return self.__str__()
        # out = f'{self.imie} {self.nazwisko}'
        # if len(self.adresy) > 0:
        #     return f'{out} {self.adresy}'
        # else:
        #     return out

class Adres():
    # def __init__(self, ulica="", miasto="", stan="", kod="", panstwo=""):
    #     self.ulica = ulica
    #     self.miasto = miasto
    #     self.stan = stan
    #     self.kod = kod
    #     self.panstwo = panstwo
    # idziemy po krawędzi - nie ważne co nam  podadzą :)
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    # wygląda na to, że jak  __repr__ ma wyglądać tak samo jak __str__, to wystarczy zaimplemenotwać tylko  __repr__
    # def __str__(self):
    #     return f'{self.miasto}'
    def __repr__(self):
        ##dzięki  temu wyświetli  każdą zmienną !!!
        return f'{self.__dict__}'


neil = Kontakt(imie='Neil', nazwisko='Armstrong')
print(neil)
# Neil Armstrong

alan = Kontakt(imie='Alan', nazwisko='Shepard', adresy=[Adres(miasto='Houston'), Adres(miasto='Cocoa Beach')])
print(alan)
# Alan Shepard [Houston, Cocoa Beach]



ksiazka_adresowa = [
    Kontakt(imie='Max', nazwisko='Peck', adresy=[
        Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Adres(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Adres(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Adres(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
    ]),
    Kontakt(imie='José', nazwisko='Jiménez'),
    Kontakt(imie='Иван', nazwisko='Иванович', adresy=[]),
]

print(ksiazka_adresowa)
# [Max Peck [Houston, Kennedy Space Center, Pasadena, Palmdale], José Jiménez, Иван Иванович]