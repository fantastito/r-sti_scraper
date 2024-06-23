from bs4 import BeautifulSoup
import requests

url = "https://www.lidl.co.uk/c/food-offers/s10023092"
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")

target_text = "Flavour of the Week: Sol Y Mar"
flavour_of_the_week = soup.find('h3', string=lambda t:t and target_text in t)

# for offer in soup.find_all('h3'):
#     print(offer)

# for date in soup.find_all("p"):
#     print(date)
if flavour_of_the_week:
    print("It's Spanish week!")
# <h3 class="ATheContentPageCard__Claim">Flavour of the Week: Sol Y Mar</h3>