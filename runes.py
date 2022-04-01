from bs4 import BeautifulSoup
import requests
from PIL import Image
import urllib.request

def runes(arg1,arg2):
    url = 'https://www.op.gg/champion/{}/statistics/{}/rune'.format(arg1,arg2)

    result = requests.get(url)
    doc= BeautifulSoup(result.content, "html.parser")


    allrunes = doc.find('div', 'perk-page-wrap')
    runes = []


    runestext = allrunes.find_all('div', 'perk-page__item--active')
    for a in runestext:
        runeimages = a.find_all('img')
        for b in runeimages:
            runes.append("https:" + b['src'])

    images = []
    imagesizes = []
    for c in range (0, len(runes)):
        urllib.request.urlretrieve(runes[c], str(c) + ".png")
        images.append(Image.open(str(c) + ".png"))
        images[c] = images[c].resize((128, 128), Image.ANTIALIAS)
        imagesizes.append(images[c].size)

    runeimages = Image.new('RGBA',(len(images)*128, 128), (256,256,256))


    for d in range(0, len(images)):
        runeimages.paste(images[d],(d*imagesizes[d][0],0))

    runeimages.save("runes.png")
