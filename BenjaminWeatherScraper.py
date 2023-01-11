import requests #requests gathers information from a given webpage
from bs4 import BeautifulSoup #BeautifulSoup parses HTML files gathered from requests
lat = input("Enter a latitude coordinate")
lon = input("Enter a longitude coordinate")
toget = "https://forecast.weather.gov/MapClick.php?lat="+lat + "&lon=" + lon
print(toget)
url = requests.get(toget)
#url = requests.get("https://forecast.weather.gov/MapClick.php?lat=41.884250000000065&lon=-87.63244999999995") #the link to this webpage takes a set of coordinates as arguments
soup = BeautifulSoup(url.content,features="html.parser") #assigns all the content of that page to the variable "soup"
#print(soup.prettify()) #we can use prettify() to display all html code in an easy-to-view format
#tds = soup.find_all("td") #finds everything on the page with the tags <td></td>, stores it as the list "tds"
#print(soup.prettify)
location = soup.find("h2","panel-title")
print(location.text)
# days = soup.find_all("p","period-name")
# print(days)
def SevenDayForecast(soup):
    days = soup.find_all("p","period-name") #finds every <p></p> tag with the class "period-name", used on the site to list days
    desc = soup.find_all("p","short-desc") #finds every day's description
    hightemp = soup.find_all("p","temp temp-high")
    lowtemp = soup.find_all("p","temp temp-low")
    # for de in desc:
    #      print(de)
    temps = []
    for i in range(len(hightemp)): #adds every temperature reading to the same list, alternating high temps and low temps
        try:
            temps.append(hightemp[i].text)
            temps.append(lowtemp[i].text)
        except(IndexError):
            pass
    #print(temps)
    #print("Desc:",len(desc),"Days:",len(days),"High Temp",len(hightemp),"Low Temp",len(lowtemp),len(temps))
    print(days)

    for i in range(len(days)):
        day = days[i].text
        des = desc[i].text
        if "Night" in day:#if there is a "Night" in the day, like "WednesdayNight", this adds a space between the day and the word Night
            loc = day.find("N")
            day= day[:loc] + " " + day[loc:]
        if "then" in des: #ditto for any instances of the word "then" in a weather description
            loc = des.find("then")
            des = des[:loc]+ " " + des[loc:]

        print(day + ":", des, temps[i])
        print()
        # if "night" in days[i].text.lower():
        #     print("test")
SevenDayForecast(soup)