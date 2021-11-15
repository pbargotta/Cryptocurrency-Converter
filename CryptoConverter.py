import requests
from bs4 import BeautifulSoup
from math import log10, floor


def round_sig(x, sig=2):
    return round(x, sig - int(floor(log10(abs(x)))) - 1)


URL = "https://bitcourier.co.uk/prices"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
cryptoElements = soup.find_all("tr", class_="border-t border-gray-200 hover:bg-yellow-50 transition ease-in-out "
                                            "duration-150")

prices = []
for cryptoElements in cryptoElements:
    nameElement = cryptoElements.find("span", class_="inline-block align-middle").text.strip()
    priceElement = cryptoElements.find("a", class_="text-indigo-600 hover:text-indigo-500 hover:underline").text.strip()

    if nameElement == "btc":
        prices.append(priceElement)
    elif nameElement == "eth":
        prices.append(priceElement)
    elif nameElement == "doge":
        prices.append(priceElement)

bitcoinValue = float(prices[0].translate({ord(i): None for i in '£,'}))
ethereumValue = float(prices[1].translate({ord(i): None for i in '£,'}))
dogecoinValue = float(prices[2].translate({ord(i): None for i in '£,'}))

convertTo = input("What would you like to convert to? ").lower()
gbp = float(input("How much would you like to convert? "))

if convertTo == "bitcoin" or convertTo == "b":
    print(round_sig((gbp / bitcoinValue), 2), "BTC")
elif convertTo == "ethereum" or convertTo == "e":
    print(round_sig((gbp / ethereumValue), 2), "ETH")
elif convertTo == "dogecoin" or convertTo == "d":
    print(round_sig((gbp / dogecoinValue), 2), "DOGE")
else:
    print("Please pick a valid cryptocurrency next time. ")