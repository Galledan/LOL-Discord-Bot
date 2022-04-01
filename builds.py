from bs4 import BeautifulSoup
import requests
from PIL import Image
import PIL
import urllib.request
import sys

def items(arg1,arg2):
    url = 'https://www.op.gg/champion/{}/statistics/{}'.format(arg1, arg2)
    
    result = requests.get(url, headers=headers)
    doc= BeautifulSoup(result.content, "html.parser")

    allitems = doc.find_all('td', 'champion-overview__data champion-overview__border champion-overview__border--first')
    unwanted = "//opgg-static.akamaized.net/images/site/champion/blet.png"


    #Starting Items
    startingitems = []


    for i in range(0, 2):
        itemimages = allitems[i].find_all('img')
        for a in range(0, len(itemimages)):
            if(itemimages[a]['src'] != unwanted):
                    startingitems.append("https:" + itemimages[a]['src'])

    images = []
    imagesizes = []
    for c in range (0, len(startingitems)):
        urllib.request.urlretrieve(startingitems[c], str(c) + ".png")
        images.append(Image.open(str(c) + ".png"))
        imagesizes.append(images[c].size)

    startingimages = Image.new('RGB',(len(images)*imagesizes[0][0], imagesizes[0][1]), (250,250,250))

    for d in range(0, len(images)):
        startingimages.paste(images[d],(d*imagesizes[d][1],0))

    startingimages.save("starting.png")

    #Suggested Items
    suggesteditems = []

    for i in range(2, len(allitems)):
        itemimages = allitems[i].find_all('img')
        for a in range(0, len(itemimages)):
            if(itemimages[a]['src'] != unwanted):
                if("https:" + itemimages[a]['src'] not in suggesteditems):
                    suggesteditems.append("https:" + itemimages[a]['src'])

    images = []
    imagesizes = []
    for c in range (0, len(suggesteditems)):
        urllib.request.urlretrieve(suggesteditems[c], str(c) + ".png")
        images.append(Image.open(str(c) + ".png"))
        imagesizes.append(images[c].size)

    suggestedimages = Image.new('RGB',(len(images)*imagesizes[0][0], imagesizes[0][1]), (250,250,250))

    for d in range(0, len(images)):
        suggestedimages.paste(images[d],(d*imagesizes[d][1],0))

    suggestedimages.save("suggested.png")






