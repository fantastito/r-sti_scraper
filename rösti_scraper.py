import json
from bs4 import BeautifulSoup
import requests

##Find alpine week

url = "https://www.lidl.co.uk/c/food-offers/s10023092"

def check_for_rösti():
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        #Find this week's offers section
        this_week = soup.find(title="This Week's Offers")

        target_text = "Flavour of the Week"

        #Find the 'Flavour of the Week' card by searching h3 tags for target with string, checking string not empty
        flavour_of_the_week = this_week.find('h3', string=lambda t:t and target_text in t)
        for child in flavour_of_the_week.children:
            print(child)
            if 'Alpen Fest' in child:
                return True
            else:
                return False



check_for_rösti()

