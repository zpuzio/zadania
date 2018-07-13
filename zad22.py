from collections import Counter


file1 = open("name.txt", "r")
wordcount1 = Counter(file1.read().split())
print wordcount1

#for pair in wordcount.items():
    #print(pair)
for x,y in wordcount1.items():
    print x,y

#---------------------------------------------------------------

word = []
lines = [line.rstrip('\n') for line in open('this.txt')]
r = range(0,len(lines))

with open("category.txt", "w") as open_file:
    for i in r:
        word.append(lines[i].split("/"))
        open_file.write(word[i][2])
        open_file.write("\n")

file = open("category.txt", "r")
wordcount = Counter(file.read().split())
# print wordcount

for x,y in wordcount.items():
    print x,y