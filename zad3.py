a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b =[]
for i in a:
    if i<5:
        b.append(i)
print b

c =[i for i in a if i<5]
print c

number = int(raw_input("Podaj liczbe: "))

d = [i for i in a if i<number]
print d