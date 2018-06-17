meters = int(input("podaj ilość metrów: "))

def conv_dist (meters: int) -> dict:
    km = int(meters / 1000)
    mil = float(meters / 1608)
    nmil = float(meters / 1852)

    return{"kilometers":km,
           "miles":mil,
           "nautical miles":nmil,
           "all":[km,mil,nmil]
           }

res_dict = conv_dist(meters)
# takie tam dodanie elementu do słownika
# res_dict["test"]= 0

for klucz in res_dict.keys():
    print(klucz, res_dict[klucz])
