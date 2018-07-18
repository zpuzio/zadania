from bokeh.plotting import figure, show, output_file
from bokeh.models.annotations import Title
import json
from collections import Counter
months = {1:"styczen" ,2: "luty" ,3: "marzec" ,4: "kwiecien" ,
            5: "maj" ,6: "czerwiec" ,7: "lipiec" ,8: "sierpien" ,
            9: "wrzesien" ,10: "pazdziernik" ,11: "listopad" ,12: "grudzien"}

items = []
with open('birthday.json', 'r') as f:
    birthday = json.load(f)
for item in birthday.values():
    a = item.split("/")
    items.append(a[1])
count = Counter(items)
result = {}
"""
for x in count.keys():
        result = {months[int(x)]: count[x]}
        print count[x]
        #birthday.update({person: date})
"""
result = {months[int(x)]: count[x] for x in count.keys()}

print(result.keys())
output_file("plot.html")
categories = list(months.values())
print(categories)
x = list(result.keys())
y = list(count.values())

p = figure(x_range=categories)
p.vbar(x=x, top=y, width=0.5)

p.xaxis.axis_label = 'Miesiace'
p.yaxis.axis_label = 'Liczba naukowcow'
t = Title()
t.text = 'Moja figura'
p.title = t
show(p)
"""
for x in birthday.keys():
   type(x.encode('utf-8'))
"""