def last(a):
    a = [5, 10, 15, 20, 25]
    d = len(a)-1
    c = [a[0],a[d]]
    print c
    return c

def main():
    lista = [5, 10, 15, 20, 25]
    wynik = last(lista)
    print type(wynik)
main()