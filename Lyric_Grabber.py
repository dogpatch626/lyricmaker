import requests, pprint
from bs4 import  BeautifulSoup 
import random
#htmlF= 'https://genius.com/Frank-ocean-godspeed-lyrics'

search = input("what song do u want in genius url format")
response1 = requests.get('https://genius.com/'+search)
response2 = requests.get('https://genius.com/Madvillain-accordion-lyrics')
response = requests.get('https://genius.com/Kanye-west-ghost-town-lyrics')
resp = 'https://genius.com/' + search
#print(resp)

# 

soup = BeautifulSoup(response.text, 'html.parser')# parse to page 
soup2 = BeautifulSoup(response2.text, 'html.parser')
lyrics = []
lyrics2 = []
x = 0


for br in soup.findAll('br'):
    next_s = br.nextSibling
    lyrics.append(next_s)  

for br in soup2.findAll('br'):
    next_s = br.nextSibling
    lyrics2.append(next_s)  
    #print(next_s)
    #print(lyrics[x])
    #x+=1
#list(map(str.strip,lyrics))


t = list(map(lambda s: s.strip(), lyrics))
y = list(map(lambda s: s.strip(), lyrics2))
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(lyrics2)
#print(y)
for i in range (24):
    x = random.randint(1, len(t)-1)
    g = random.randint(1, len(y)-1)
    print(i, t[x])
    print(i+1, y[g])
#print(soup.get_text())
#print(lyrics)