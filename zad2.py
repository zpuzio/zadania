number = int(raw_input("Podaj cyfre: "))
if number%2 == 0:
    print("Liczba parzysta")
else:
    print "Liczba nieparzysta"

if number%4 == 0:
    print "Liczba podzielna przez 4"

licznik = int(raw_input("Podaj licznik: "))
mianownik = int(raw_input("Podaj mianownik: "))

if licznik%mianownik == 0:
    print "Licznik jest podzielny przez mianownik"
else:
    print "Licznik nie jest podzielny przez mianownik"