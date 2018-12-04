import requests
from bs4 import BeautifulSoup

resp = requests.get("http://140.112.147.120/pyHumanities/sample.html")
page = BeautifulSoup(resp.text, "html.parser")
h1_elems = page.find_all("h1")
a_elem = page.find("a")

print("h1_elems: {}".format(h1_elems))
print("a_elem text: {}".format(a_elem.text))
print("a_elem href: {}".format(a_elem.get("href")))
