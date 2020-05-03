'''I created a web scraping project in which it scrap hacker news site. in this project we can get only those titles which having rating of 100 or more than 100 ratings'''
from bs4 import BeautifulSoup
import requests
import pprint
responce = requests.get('https://news.ycombinator.com')#here we take responce from the url or we can say get the url
soup = BeautifulSoup(responce.text, 'html.parser')#making an object of Beautifulsoup which  take the html text of site.
links = soup.select('.storylink') #we select storylink class which contain link title etc through select method
subtext = soup.select('.subtext') #select subtext class which contain score

#created a function which take links and subtext and retuen a list which contain title link or votes
def create_custom_hn(links, subtext):
     hn = []
     for idx,item in enumerate(links):
         title = links[idx].getText() #we get title from this
         href = links[idx].get('href', None) #we get link from this
         vote = subtext[idx].select('.score') #we select score class
         if len(vote): #here we use if because not every titles contain votes
            points = int(vote[0].getText().replace('points', '')) #here we get the points
            if points>99: #we chose only those titles which is having votes more than 99
                hn.append({'title': title, 'link': href, 'votes': points})  #we append the title links votes here
     return sorted(hn, key=lambda k:k['votes'], reverse=True) #we sort data in decreasing order

pprint.pprint(create_custom_hn(links, subtext))