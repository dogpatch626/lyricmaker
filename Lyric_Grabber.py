import requests, pprint
from bs4 import  BeautifulSoup 
#htmlF= 'https://genius.com/Frank-ocean-godspeed-lyrics'
response = requests.get('https://genius.com/Frank-ocean-godspeed-lyrics')
soup = BeautifulSoup(response.text, 'html.parser')
lyrics = []
x = 0
#print(response.text)

#print(soup.prettify())
#for lyric in soup.find_all('br'):
#for a in soup.find_all('a'):
for br in soup.findAll('br'):
        next_s = br.nextSibling
        lyrics.append(next_s)    
    #print(next_s)
    #print(lyrics[x])
    #x+=1
#list(map(str.strip,lyrics))
t = list(map(lambda s: s.strip(), lyrics))
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(t)
#print(soup.get_text())
#print(t)