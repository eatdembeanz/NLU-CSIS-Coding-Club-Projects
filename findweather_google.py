from bs4 import BeautifulSoup
import requests
url = "https://weather.com/weather/today/l/624f0cccc10bececfa4c083056cef743837a76588790f476c9ebea44be35e51f"
url2 = "https://www.google.com/search?q=chicago+weather"
cont = requests.get(url)
cont2 = requests.get(url2)
res = requests.get(f'https://www.google.com/search?q=chicago+weather&oq=chicago+weather&aqs=chrome.0.69i59j0i131i433i512l2j0i433i512j0i512j0i131i433i512j0i512j69i60.3064j1j7&sourceid=chrome&ie=UTF-8')
stuff = BeautifulSoup(res.text,features="html.parser")
#print(stuff.prettify())
#templist = stuff.find_all(attrs={'data-testid':'TemperatureValue'}) #looking for data-testid="TemperatureValue"
weather = stuff.select('#wob_tm')[0].getText().strip()

#, attrs={'id':'wob_tm'}
#name='span', attrs={'class':'wob_t q8U8x'
#print(templist[0])
#print(type(templist[0]))
print(weather)