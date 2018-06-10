user_input = ""
while True:
    try:
        user_input = float(input("zapodaj wiek: "))
        if user_input >= 0:
            break
    except ValueError:
        print("nie wygłupiaj się. podaj wiek")
        continue

#good practice: nie wpisujemy liczb czy innych rzeczy z palucha. Tworzymy na to  zmienne lub stałe, które oczywiście mogą być wcześniej  policzone czy cośtam
ADULT_AGE = 18

#używamy naszej wcześniej stałej / zmiennej, a nie "magic number"
if user_input >= ADULT_AGE:
    print("możesz wejść")
else:
    print("przyjdź z mamą")