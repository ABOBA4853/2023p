import requests
from colorama import init, Fore


class CurrencyConverter:

   def __init__(self):

       self.rates = {}

   def get_rates(self):

       response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

       data = response.json()

       for item in data:

           self.rates[item['cc']] = item['rate']

   def convert(self, amount, from_currency, to_currency):

       if from_currency != "USD":

           amount = amount / self.rates[from_currency]

       amount = round(amount * self.rates[to_currency], 2)

       return amount

converter = CurrencyConverter()

converter.get_rates()

while True:

   try:

       amount = float(input(Fore.BLUE + "Введіть суму валюти: "))

       from_currency = input(Fore.BLUE + "Введіть код валюти введеної суми: ")

       to_currency = "USD"

       converted_amount = converter.convert(amount, from_currency.upper(), to_currency)

       print(Fore.YELLOW + "The amount of {} {} is equal to {:.2f} USD".format(amount, from_currency.upper(), converted_amount))

       break

   except KeyError:

       print("Введено недійсний код валюти. Будь ласка спробуйте ще раз.")

   except ValueError:

       print(Fore.BLUE + "Введено невірну суму. Будь ласка спробуйте ще раз.")