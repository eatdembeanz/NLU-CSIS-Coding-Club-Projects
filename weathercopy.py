import requests
from bs4 import BeautifulSoup
url = requests.get("https://google.com/search?q=weather+chicago")
soup = BeautifulSoup(url.content,features="html.parser")
print(soup.prettify())
# currentemp = soup.find("div",attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
# print("Your current weather is", currentemp)
# city = soup.find("span",attrs={"class":"BNeawe tAd8D AP7Wnd"}).text
# print("Your city is", city)

