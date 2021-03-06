from bs4 import BeautifulSoup
from discord.enums import PremiumType
import requests
from requests.sessions import default_headers

def pro(arg):

    url = "https://www.leagueofgraphs.com/tr/summoner/tr/{}".format(arg)

    result = requests.get(url)
    doc= BeautifulSoup(result.content, "html.parser")
    bestLeagueDoc = doc.find('div', 'best-league')
    profilePicDoc = doc.find('div' ,'pageBanner img-align-block')
    champDoc = doc.find_all('td', 'champColumn')
    kdaDoc= doc.find('div', 'number')
    laneDoc = doc.find('div', id='profileRoles')
    allLanes = laneDoc.find_all('div', 'txt name')
    levelText = doc.find('div', 'bannerSubtitle').next_element
    flexDoc = doc.find('div', 'medium-16 small-20 columns rankLine')
    flexWinDoc = doc.find('div', 'medium-12 small-12 columns text-right requireTooltip')
    

    level = levelText[48:52]
    kill = kdaDoc.find('span' , 'kills').string
    death = kdaDoc.find('span' , 'deaths').string
    assist = kdaDoc.find('span' , 'assists').string
    profilePic = profilePicDoc.find('img')['src']
    tier = doc.find('div','leagueTier').string
    flexTier = doc.find('div', 'medium-14 columns leagueTier').string
    lp = doc.find('span','leaguePoints').string
    flexlp = doc.find('div', 'medium-8 small-4 columns text-right').find('span', 'leaguePoints').string
    winNum = doc.find('span','winsNumber').string
    flexwinNum = flexWinDoc.find('span','winsNumber').string
    loseNum = doc.find('span','lossesNumber').string
    flexloseNum = flexWinDoc.find('span','lossesNumber').string
    tierPic = bestLeagueDoc.find('img')['src']
    winRate = doc.find('div', id='graphDD4').string
    rank = doc.find('span', 'highlight').string
    flexrank = flexDoc.find('span', 'highlight-dark-only').string
    regionalRank = doc.find('a', 'regionalRank').string
    flexregionalRank = flexDoc.find('div', 'regionalRank').a.string

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
    
    
    return level,kill,death,assist,profilePic,tier,flexTier,lp,flexlp,winNum,flexwinNum,loseNum,flexloseNum,tierPic,winRate,rank,flexrank,regionalRank,flexregionalRank ,champListTop5,champListRest,mainLanes
