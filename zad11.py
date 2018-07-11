def prime():
    number = int(raw_input("Podaj cyfre: "))
    x = range(2, number)

    if number == 1:
         prime = True
    if number == 2:
        prime = True
    else:
        prime = True
        for i in x:
            if number%i == 0:
                prime = False
    if prime == False:
        print "Liczba nie jest pierwsza"
    elif prime == True:
        print "Liczba pierwsza"

d = prime()