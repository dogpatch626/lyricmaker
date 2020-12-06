import requests, pretty
from bs4 import  BeautifulSoup 
htmlF= 'https://genius.com/Joji-and-benee-afterthought-lyrics'
response = requests.get('https://genius.com/Joji-and-benee-afterthought-lyrics')
soup = BeautifulSoup(response.text, 'html.parser')


#print(response.text)

#print(soup.prettify())
#for lyric in soup.find_all('br'):
for br in soup.findAll('br'):
    next_s = br.nextSibling
    print(next_s)

#print(soup.get_text())