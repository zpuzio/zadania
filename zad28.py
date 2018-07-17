def maximum(a,b,c):
    if a < b:
        if c < b:
            print "Wartosc maksymlana: " + str(b)
            return b
        else:
            print "Wartosc maksymlana: " + str(c)
            return c
    else:
        if a > c:
            print "Wartosc maksymlana: " + str(a)
            return a
        else:
            print "Wartosc maksymlana: " + str(c)
            return c
if __name__=="__main__":
    n1 = int(raw_input("Podaj cyfre: "))
    n2 = int(raw_input("Podaj cyfre: "))
    n3 = int(raw_input("Podaj cyfre: "))
    maximum(n1, n2, n3)