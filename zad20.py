def element_search(lista, number):
    lista = sorted(lista)
    #print lista
    ist = False
    if number in lista:
        #print "Liczba znajduje sie w liscie"
        ist = True
    return ist

def binary_search(lista, number):
    lista = sorted(lista)
    if len(lista) == 0:
        return False
    else:
        d = len(lista)/2
        if lista[d] == number:
            return True
        else:
            if number > lista[d]:
                return binary_search(lista[d+1:],number)
            else:
                return binary_search(lista[:d],number)


if __name__=="__main__":
    l = [1,3,2,1,5,6,9,11]
    n = int(raw_input("Podaj liczbe: "))
    #print element_search(l,n)
    print binary_search(l, n)