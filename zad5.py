import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#print len(a)
#print len(b)

d = []

for i in a:
    if i in b:
        if i not in d:
            d.append(i)
print d

a1 = random.sample(xrange(300),13)
b1 = random.sample(xrange(300),9)
print a1
print b1

d1 = []

for i in a1:
    if i in b1:
        if i not in d1:
            d1.append(i)
print d1