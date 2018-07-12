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
    d = len(lista)/2
    if a[d]>number:
        lista = lista[:d]





if __name__=="__main__":
    l = [1,3,2,1,5,6,9,11]
    n = int(raw_input("Podaj liczbe: "))
    print element_search(l,n)