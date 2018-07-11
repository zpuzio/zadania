import random

a = random.randint(1,9)

number = int(raw_input("Podaj cyfre od 1 do 9: "))
if number>a:
    print "Za duza"
elif number < a:
    print "Za mala"
else:
    print "Zgadles"

#print a