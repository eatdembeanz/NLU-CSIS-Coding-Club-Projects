from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def city():
   def weather(city):
      city = city.replace("", "+")

res=requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0. i635i39l2j0l4j46j690.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)

soup = BeautifulSoup(res.text,'html.parser')

# location = soup.select('#wob_loc')[0].getText().strip()
if len(soup.select('#wob_loc')) > 0:
    location = soup.select('#wob_loc')[0].getText().strip()
else:
    location = None


# time = soup.select('#wob_dts')[0].getText().strip()
if len(soup.select('#wob_dts')) > 0:
    time = soup.select('#wob_dts')[0].getText().strip()
else:
    time = None


# info = soup.select('#wob_dc')[0].getText().strip()
if len(soup.select('#wob_dc')) > 0:
    info = soup.select('#wob_dc')[0].getText().strip()
else:
    info = None

# weather = soup.select('#wob_tm')[0].getText().strip()
if len(soup.select('#wob_tm')) > 0:
    weather = soup.select('#wob_tm')[0].getText().strip()
else:
    print("no city found")

print("enter the city name")
city = input()
city = city + 'weather'
weather(city)



