import requests
from bs4 import BeautifulSoup


# Der Fremde - Ludwig Tieck
url1="https://www.projekt-gutenberg.org/tieck/fremde/chap001.html"

def textscrape(filename, url):

    raw = requests.get(url)
    raw.encoding='utf-8'
    soup = BeautifulSoup(raw.text, 'html.parser')
    ptags=soup.find_all('p')

    text = '\n'.join([p.get_text() for p in ptags])
    tex=text.replace('\xa0','')
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(tex)
#lediglich zur einmaligen Benutzung gedacht
#textscrape("test.txt", url1)

#notiz:
# - händische nachkorrektur der texte notwendig, da die p-tags von der website so komisch sind >:-(
# - ich musste scrapen, da falsche gutenberg seite (html und nicht txt)
# - nachkorrektur: es musste nur der fremde gescraped werden, da die restlichen texte unter textgridrep.org  verfügbar waren