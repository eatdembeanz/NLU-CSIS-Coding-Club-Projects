import requests #requests gathers information from a given webpage
from bs4 import BeautifulSoup #BeautifulSoup parses HTML files gathered from requests
url = requests.get("https://forecast.weather.gov/MapClick.php?lat=41.884250000000065&lon=-87.63244999999995") #the link to this webpage takes a set of coordinates as arguments
soup = BeautifulSoup(url.content,features="html.parser") #assigns all the content of that page to the variable "soup"
print(soup.prettify()) #we can use prettify() to display all html code in an easy-to-view format
tds = soup.find_all("td") #finds everything on the page with the tags <td></td>, stores it as the list "tds"
#print(tds)
# print(tds[0])
# print(tds[0].text)
for i in tds: #loops through the tds list, every item is an instance of the <td></td> tag
   print(i.text) #prints the text of the instance

# currentemp = soup.find("div",attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
# print("Your current weather is", currentemp)
# city = soup.find("span",attrs={"class":"BNeawe tAd8D AP7Wnd"}).text
# print("Your city is", city)

