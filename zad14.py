def delete_duplicate(a):
    print type(a)
    print "Pierwotna lista" + str(a)
    aa = set(a)
    print "Nowa lista " + str(aa)
    return list(aa)

def delete_duplicate_loop(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print b
    return list(b)

def main():
    c = [1,1,3,3,3,6,7,7,8,9,9,9,9,9,12,15]
    wynik = delete_duplicate(c)
    print(type(wynik))
    wynik1 = delete_duplicate_loop(c)
    print(type(wynik1))

main()