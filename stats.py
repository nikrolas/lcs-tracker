import praw
import re
from termcolor import colored, cprint
import requests
import sys
from bs4 import BeautifulSoup
import urllib.request

user_agent = ("LCS games/highlights")
r = praw.Reddit(user_agent=user_agent)


def login():
    r.login('nikrolasnicky', 'sonko', disable_warning=True)

    print_login = colored("Logging in...\n", 'yellow')
    print(print_login)

def lcsgamesvideos():
    print_input1 = colored("Which team are you looking for? \n")
    team = input(print_input1).upper()
    if team in {"TSM", "CLG", "APX", "TL", "NRG", "IMT", "NV", "C9", "FOX", "P1"}:
        req = urllib.request.Request("https://www.reddit.com/r/LoLeventVoDs/comments/4mfr9f/na_lcs_2016_summer_split/", headers={'User-Agent': 'Mozilla/5.0'})
    elif team in {"FNC", "OG", "G2" , "H2K", "ROC", "S04", "UOL", "GIA", "SPY", "VIT"}:
        req = urllib.request.Request("https://www.reddit.com/r/LoLeventVoDs/comments/4m50qp/eu_lcs_2016_summer_split/", headers={'User-Agent': 'Mozilla/5.0'})
    else:
        print ("No such team!")
        sys.exit
    webpage = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    counter = int (0);
    for tbody in soup.find_all('tbody'):
        for tr in tbody.find_all('tr'):
            tds = tr.find_all('td')
            if tds[1].find('strong').text == team or tds[3].find('strong').text == team:
                if counter != 3 :
                    counter = counter + 1
                else: counter = 1
                print (colored(tds[1].text + " " + tds[2].text + " " + tds[3].text + " Game " + str(counter), 'red'))
                print ('Pick + Bans: ' + tds[5].find('a').get('href'))
                print ('Game Start: ' + tds[6].find('a').get('href'))
                print('Highlights" ' + tds[7].find('a').get('href'))
        counter = 0
lcsgamesvideos()


