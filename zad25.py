def binary_search(lista,c):
    if len(lista) == 1:
        print "Podana przez Ciebie liczba to: " + str(lista[0])
    else:
        d = len(lista) / 2
        c += 1
        odp = raw_input("Czy liczba " + str(lista[d]) + " jest za wysoka, za mala czy dobra [d/m/ok]:  ")
        if odp == "m":
            return binary_search(lista[d + 1:], c)
        elif odp == "d":
            return binary_search(lista[:d], c)
        else:
            print "Podana przez Ciebie liczba to: " + str(lista[d])
            print "Liczba zgadniec: " + str(c)

if __name__=="__main__":
    print("Program ma zgadnac liczbe od 0 do 100")
    lista = range(0,101)
    c = 0
    binary_search(lista,c)