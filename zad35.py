import json
from collections import Counter

items = []
months = {1:"styczen" ,2: "luty" ,3: "marzec" ,4: "kwiecien" ,
            5: "maj" ,6: "czerwiec" ,7: "lipiec" ,8: "sierpien" ,
            9: "wrzesien" ,10: "pazdziernik" ,11: "listopad" ,12: "grudzien"}
with open('birthday.json', 'r') as f:
    birthday = json.load(f)
for item in birthday.values():
    a = item.split("/")
    items.append(a[1])
count = Counter(items)
print count

for x in count.keys():
    print {months[int(x)]:count[x]}
