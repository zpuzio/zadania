def fibonnaci(number):
    x = range(0,number)
    a = []
    for i in x:
        if x.index(i)==0 or x.index(i)==1:
            a.append(1)
        else:
            a.append(a[i-1]+a[i-2])
    print a
f = fibonnaci(9)