from textwrap import wrap
import requests
from bs4 import BeautifulSoup

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")
#print soup.get_text()
f = raw_input("Jak chcesz nazwac plik txt: ")

with open(f, "w") as open_file:
    for x in soup.find_all(class_="content-section"):
        for p in x.find_all("p"):
            a = p.get_text()
            a = "\n".join(wrap(a))
            open_file.write(a.encode("utf-8"))

