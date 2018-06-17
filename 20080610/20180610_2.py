user_input = ""
while True: #not isinstance(user_input, (int, float)):
    try:
        user_input = float(input("zapodaj liczbę: "))
        user_input = int(user_input)
        break
    except ValueError:
        print("nie wygłupiaj się. podaj liczbę")
        # user_input = float(input("zapodaj liczbę: "))
        continue

if divmod(user_input, 2)[1] == 1:
    print("liczba nieparzysta")
else:
    print("liczba parzysta")