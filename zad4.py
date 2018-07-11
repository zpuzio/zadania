number = int(raw_input("Podaj cyfre: "))
x = range(1,number+1)
#print x
l = []
for i in x:
    if number%i == 0:
        l.append(i)
print l