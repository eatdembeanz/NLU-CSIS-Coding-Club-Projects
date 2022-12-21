import requests
from bs4 import BeautifulSoup
url = requests.get("https://forecast.weather.gov/MapClick.php?lat=41.884250000000065&lon=-87.63244999999995")
soup = BeautifulSoup(url.content,features="html.parser")
#print(soup.prettify())
tds = soup.find_all("td")
#print(tds)
# print(tds[0])
# print(tds[0].text)
for i in tds:
   print(i.text)

# currentemp = soup.find("div",attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
# print("Your current weather is", currentemp)
# city = soup.find("span",attrs={"class":"BNeawe tAd8D AP7Wnd"}).text
# print("Your city is", city)

