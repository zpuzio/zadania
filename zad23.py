with open('prime.txt', 'r') as f1:
    t1 = f1.read().splitlines()

with open('happy.txt', 'r') as f2:
    t2 = f2.read().splitlines()

print sorted(set(t1).intersection(t2))




