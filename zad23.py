with open('prime.txt', 'r') as f1:
    t1 = f1.read().splitlines()

with open('happy.txt', 'r') as f2:
    t2 = f2.read().splitlines()

c = []
for i in t1:
    if i in t2:
        c.append(i)
print c



