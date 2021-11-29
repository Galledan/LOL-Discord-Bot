from bs4 import BeautifulSoup
from discord.enums import PremiumType
import requests
from requests.sessions import default_headers

def pro(arg):

    url = "https://www.leagueofgraphs.com/tr/summoner/tr/{}".format(arg)

    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.91'
    }

    result = requests.get(url, headers=headers)
    doc= BeautifulSoup(result.content, "html.parser")
    bestLeagueDoc = doc.find('div', 'best-league')
    profilePicDoc = doc.find('div' ,'pageBanner img-align-block')
    champDoc = doc.find_all('td', 'champColumn')
    kdaDoc= doc.find('div', 'number')
    laneDoc = doc.find('div', id='profileRoles')
    allLanes = laneDoc.find_all('div', 'txt name')
    levelText = doc.find('div', 'bannerSubtitle').next_element
    

    level = levelText[48:52]
    kill = kdaDoc.find('span' , 'kills').string
    death = kdaDoc.find('span' , 'deaths').string
    assist = kdaDoc.find('span' , 'assists').string
    profilePic = profilePicDoc.find('img')['src']
    tier = doc.find('div','leagueTier').string
    queue = doc.find('span','queue').string
    lp = doc.find('span','leaguePoints').string
    winNum = doc.find('span','winsNumber').string
    loseNum = doc.find('span','lossesNumber').string
    tierPic = bestLeagueDoc.find('img')['src']
    winRate = doc.find('div', id='graphDD4').string
    rank = doc.find('span', 'highlight').string
    regionalRank = doc.find('a', 'regionalRank').string

    champListTop5 = []
    champListRest = []

    for i in range(0,5):
        a= str(i+1) + "-" + champDoc[i].find('div', 'name').string
        champListTop5.append(a)

    for i in range(5,10):
        a= str(i+1) + "-" + champDoc[i].find('div', 'name').string
        champListRest.append(a)


    champListTop5 = '\n'.join(champListTop5)
    champListRest = '\n'.join(champListRest)


    mainLanes = []

    for i in range(0,5):
        a = allLanes[i].next_element.strip()
        mainLanes.append(a)

    mainLanes = '\n'.join(mainLanes)
    

    return level,kill,death,assist,profilePic,tier,queue,lp,winNum,loseNum,tierPic,winRate,rank,regionalRank,champListTop5,champListRest,mainLanes