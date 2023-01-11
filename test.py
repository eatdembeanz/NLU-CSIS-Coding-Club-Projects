import requests #requests gathers information from a given webpage
from bs4 import BeautifulSoup #BeautifulSoup parses HTML files gathered from requests
url = requests.get("https://www.wunderground.com/weather/us/il/evanston") #accesses Weather Underground, which takes a country (us), a state (il), and a city (evanston)
        ####TRY IT OUT FOR YOURSELF: THIS URL IS FOR EVANSTON, IL. HOW CAN WE GET IT TO WORK WITH OTHER CITIES, STATES, OR COUNTRIES?###
soup = BeautifulSoup(url.content,features="html5") #assigns all the content of that page to the variable "soup"

#print(soup.find("lib-item-box"))
#print(soup.prettify()) #we can use prettify() to display all html code in an easy-to-view format
print(soup.find_all("span", "day")) #Finds all elements on the page that belong to <span class="day">: list includes "Tonight","Tomorrow", and "Tomorrow Night"


modulelink = soup.find_all("a","module-link")       #Creates a list of all <a class=module-link> elements. Looking at the HTML with soup.prettify(), this is where the temperature and day are stored!
print(modulelink[0])
print()
print(modulelink[0].text)
##Note the difference between the two!##
        ##TRY IT OUT FOR YOURSELF: WHAT OTHER INFORMATION CAN WE GET FROM THIS PAGE? ARE THERE OTHER PAGES THAT CAN GIVE US OTHER INFORMATION?##