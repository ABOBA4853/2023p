import sqlite3 as sql
import requests
from colorama import Fore


class DBContext:
    def __init__(self, database = "", timeout = 5.0):
        self.DataBase = database
        self.TimeOut = timeout
    def Execute(self, query = ""):
        try:
            connection = sql.connect(self.DataBase, self.TimeOut)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            return cursor.fetchall()
        except Exception as ex:
            print(ex)
            connection.close()
        finally:
            connection.close()
    def Query(self, query =""):
        try:
            connection = sql.connect(self.DataBase, self.TimeOut)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            connection.close()
    def QueryMany(self, query: str, records: list):
        try:
            connection = sql.connect(self.DataBase, self.TimeOut)
            cursor = connection.cursor()
            cursor.executemany(query, records)
            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            connection.close()
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


from bs4 import BeautifulSoup

from datetime import datetime


page = requests.get("https://ua.sinoptik.ua/погода-святопетрівське")


soup = BeautifulSoup(page.content, 'html.parser')


temperature = soup.find(class_='today-temp').get_text()


now = datetime.now()

date = now.strftime("%Y-%m-%d")

time = now.strftime("%H:%M:%S")


conn.execute("INSERT INTO temperature (date, time, temperature) VALUES (?, ?, ?)", (date, time, temperature))

conn.commit()

conn.close()