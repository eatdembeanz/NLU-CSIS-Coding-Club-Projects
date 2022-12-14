from bs4 import BeautifulSoup
import requests
url = "https://weather.com/weather/today/l/624f0cccc10bececfa4c083056cef743837a76588790f476c9ebea44be35e51f"
url2 = "https://www.google.com/search?q=chicago+weather"
cont = requests.get(url)
cont2 = requests.get(url2)
stuff = BeautifulSoup(cont.content,features="html5lib")
#print(stuff.prettify())
templist = stuff.find_all('span', attrs={'data-testid':'TemperatureValue'}) #looking for data-testid="TemperatureValue"
print(type(templist[0]))
