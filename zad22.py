from collections import Counter

file1 = open("name.txt", "r")
wordcount1 = Counter(file1.read().split())
print wordcount1

for x,y in wordcount1.items():
    print x,y

#---------------------------------------------------------------
print "---"*50
word = []
category = []
lines = [line.rstrip('\n') for line in open('this.txt')]
r = range(0,len(lines))

for i in r:
    word.append(lines[i].split("/"))
    category.append(word[i][2])
print Counter(category)

