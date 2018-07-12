import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/?WT.z_jog=1&hF=t&vS=undefined'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")

title = list(soup.find_all(class_="story-heading"))
print type(title)

#print(title)
for i in title:
    # print  50*'##'
    # print i
    # print 50*'--'
    # print i.a
    # print 50 * '--'
    # print i.contents[0]
    # print 50 * '--'
    # print i.get_text()
    if i.string != None:
        print(i.string.strip())

