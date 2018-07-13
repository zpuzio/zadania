import requests
from bs4 import BeautifulSoup

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")
#print soup.get_text()

for x in soup.find_all(class_="content-section"):
    for p in x.find_all("p"):
       # print 30*"##"
        print p.get_text()
