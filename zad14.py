def duplicate():
    a = [1,1,3,3,3,6,7,7,8,9,9,9,9,9,12,15]
    print "Pierwotna lista" + str(a)
    aa = set(a)
    print "Nowa lista " + str(aa)

wynik = duplicate()

def duplicate_loop():
    a = [1, 1, 3, 3, 3, 6, 7, 7, 8, 9, 9, 9, 9, 9, 12, 15]
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print b

wynik1 = duplicate_loop()