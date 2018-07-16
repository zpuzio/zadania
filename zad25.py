def binary_search(lista, number,c):
    if len(lista) == 0:
        return False
    else:
        d = len(lista) / 2
        c += 1
        odp = raw_input("Czy liczba " + str(lista[d]) + " jest za wysoka, za mala czy dobra [d/m/ok]:  ")
        if odp == "m":
            return binary_search(lista[d + 1:], number, c)
        elif odp == "d":
            return binary_search(lista[:d], number, c)
        else:
            print "Podana przez Ciebie liczba to: " + str(lista[d])
            print "Liczba zgadniec: " + str(c)

if __name__=="__main__":
    liczba = int(raw_input("Podaj liczbe od 0 do 100 ktora mam zgadnac: "))
    lista = range(0,101)
    c = 0
    binary_search(lista,liczba,c)