import csv

FILENAME = r'csv_writer_addressbook.csv'

class Kontakt:
    def __init__(self, imie, nazwisko, adresy=[]):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adresy = adresy

    def __repr__(self):
        return f'{self.__dict__}'


class Adres:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __repr__(self):
        return f'{self.__dict__}'


ksiazka_adresowa = [
    Kontakt(imie='Max', nazwisko='Peck', adresy=[
        Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Adres(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Adres(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Adres(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA', data_urodzenia=None),
    ]),
    Kontakt(imie='José', nazwisko='Jiménez'),
    Kontakt(imie='Иван', nazwisko='Иванович', adresy=[]),
]

# #ten fragment jest bez sensu: do database[] przepisuje ksiazka_adresowa 1:1
# database = []
# for contact in ksiazka_adresowa:
#     # for x in contact.__dict__:
#     #     print("atr kontaktu: ", x)
#     # print("Kontact ", contact.__dict__)
#     database.append(contact.__dict__)
# print("książka: ", ksiazka_adresowa)
# print("db: ", database)

database = ksiazka_adresowa

##---------------------------------------------------------
# jeszcze raz przemyśleć ten temat wyciągania adresów z kontaktów
##---------------------------------------------------------

headers = set()
for dict in database:
    for key in dict.keys():
        # headers.add(key)
        # print(dict[key])
        if isinstance(dict[key], list): #czy trafiliśmy na adresy
            if len(dict[key]) > 1: #jak lista jest pusta to  olać
                for elem_dict in dict[key]: #dla każdege elementu listy adresów. każdy z tych elementów to ADRES
                    print ("obiekt: ", type(elem_dict)) #to jest Adres
# tu się kurwa pogubiłem - chuj wie dlaczego tak działa????
                    for x in elem_dict.__dict__:
                        print("Atrybut: ", x)
                        headers.add(x)
        else:
            headers.add(key)

print(headers)

'''
with open(FILENAME, mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=headers,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in database:
        writer.writerow(row)
'''