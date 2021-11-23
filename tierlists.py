from bs4 import BeautifulSoup
import requests

url = "https://tr.op.gg/champion/statistics"

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.91'
}

data = []

result = requests.get(url, headers=headers)
doc= BeautifulSoup(result.content, "html.parser")

# Getting Top Lane Tier List
toptable = doc.find('tbody', 'tabItem champion-trend-tier-TOP')
topchamps = toptable.find_all('div',"champion-index-table__name")

toptierlist = []

for i in range(0,20):
   a = (str((i+1))  + "-" + topchamps[i].string)
   toptierlist.append(a)


# Getting Mid Lane Tier List
midtable = doc.find('tbody', 'tabItem champion-trend-tier-MID')
midchamps = midtable.find_all('div',"champion-index-table__name")

midtierlist = []

for i in range(0,20):
   a = (str((i+1))  + "-" + midchamps[i].string)
   midtierlist.append(a)

# Getting Jungle Tier List
jungtable = doc.find('tbody', 'tabItem champion-trend-tier-JUNGLE')
jungchamps = jungtable.find_all('div',"champion-index-table__name")

jungtierlist = []

for i in range(0,20):
   a = (str((i+1)) + "-" + jungchamps[i].string)
   jungtierlist.append(a)

# Getting ADC Tier List
adctable = doc.find('tbody', 'tabItem champion-trend-tier-ADC')
adcchamps = adctable.find_all('div',"champion-index-table__name")

adctierlist = []

for i in range(0,20):
   a = (str((i+1))  + "-" + adcchamps[i].string)
   adctierlist.append(a)

# Getting Support Tier List
suptable = doc.find('tbody', 'tabItem champion-trend-tier-SUPPORT')
supchamps = suptable.find_all('div',"champion-index-table__name")

suptierlist = []

for i in range(0,20):
   a = (str((i+1)) + "-" + supchamps[i].string)
   suptierlist.append(a)


toptierlist = '\n'.join(toptierlist)
jungtierlist = '\n'.join(jungtierlist)
midtierlist = '\n'.join(midtierlist)
adctierlist = '\n'.join(adctierlist)
suptierlist = '\n'.join(suptierlist)