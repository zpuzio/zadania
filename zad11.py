def prime(n):
    x = range(2, n)
    if n == 1:
         prime = True
    if n == 2:
        prime = True
    else:
        prime = True
        for i in x:
            if n%i == 0:
                prime = False
    if prime == False:
        print "Liczba nie jest pierwsza"
        return  False
    elif prime == True:
        print "Liczba pierwsza"
        return True

def main():
    number = int(raw_input("Podaj cyfre: "))
    d = prime(number)
    print(type(d))
main()