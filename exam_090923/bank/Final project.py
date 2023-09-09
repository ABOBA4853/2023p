import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore

a = float(0)
print(Fore.GREEN +"Привіт,Применко Андрій Борисович, ця програма потрібна вам для конвертації валюти.")
print("Вам буде запропоновано вибір, уважно читайте та обирайте?!.")
print(Fore.GREEN +"Щоб вийти, просто напишіть нуль"+ Fore.RESET)

while True:
    def converter():
        def counter(end):
            global a
            while end!=1 and end!=2 and end!=3:
                end = int(input(Fore.RED +'Надрукуйте 1, 2 або 3: '+ Fore.RESET))

            if end == 1:
                b = str(input(Fore.MAGENTA +'Зазнач суму у UAH: '+ Fore.RESET))
                if b == "a":
                    b = a
                elif b != "a":
                    b = float(b)
                print(Fore.GREEN + f'USD = {b / USD_in_UAH}$')
                print(f'EUR = {b / EUR_in_UAH}€'+ Fore.RESET)
                c = int(input(Fore.LIGHTGREEN_EX +"Якщо вам потрібно  USD, виведіть '1', щоб  EUR, натисніть '2': "+ Fore.RESET))
                if c == 1:
                    a = b / USD_in_UAH
                elif c == 2:
                    a = b / EUR_in_UAH
            elif end == 2:
                b = str(input(Fore.MAGENTA +'Внесіть свою суму USD: '+ Fore.RESET))
                if b == "a":
                    b = a
                elif b != "a":
                    b = float(b)
                print(Fore.GREEN + f'UAH = {b * USD_in_UAH}₴')
                print(f'EUR = {b * USD_in_UAH / EUR_in_UAH}€'+ Fore.RESET)
                c = int(input(Fore.LIGHTGREEN_EX +"якщо потрібно  UAH, вивести '1', щоб  EUR, вивести '2': "+ Fore.RESET))
                if c == 1:
                    a = b * USD_in_UAH
                elif c == 2:
                    a = b * USD_in_UAH / EUR_in_UAH
            elif end == 3:
                b = str(input(Fore.MAGENTA +'Надрукуйте свою суму EUR: '+ Fore.RESET))
                if b == "a":
                    b = a
                elif b != "a":
                    b = float(b)
                print(Fore.GREEN + f'USD = {b*EUR_in_UAH / USD_in_UAH}$')
                print(f'UAH = {b*EUR_in_UAH}₴'+ Fore.RESET)
                c = int(input(Fore.LIGHTGREEN_EX +"Якщо вам потрібно  USD, виведіть '1', щоб  UAH, виведіть '2': "+ Fore.RESET))
                if c == 1:
                    a = b*EUR_in_UAH / USD_in_UAH
                elif c == 2:
                    a = b*EUR_in_UAH
            return a



        resp = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, features = "html.parser")
            soup_list = soup.find_all("td")
            res = str(soup_list[39]).split('<td data-label="Офіційний курс">')
            res = str(res[1]).split('</td>')
            USD_in_UAH = float(res[0].replace(',', '.'))

        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, features = "html.parser")
            soup_list = soup.find_all("td")
            res = str(soup_list[44]).split('<td data-label="Офіційний курс">')
            res = str(res[1]).split('</td>')
            EUR_in_UAH = float(res[0].replace(',', '.'))

        print(Fore.BLUE + f'USD in UAH = {USD_in_UAH}'+ Fore.RESET)
        print(Fore.BLUE + f'EUR in UAH = {EUR_in_UAH}'+ Fore.RESET)
        end = int(input(Fore.LIGHTGREEN_EX +"Виберіть конвертер, якщо вам потрібно з UAH в USD і EUR введіть 1, з USD в UAH і EUR введіть 2, з EUR в USD і UAH введіть 3:"+ Fore.RESET))
        if end == 0:
            sys.exit()
        counter(end)









    def calculator():
        def checker(example):
            def checker(*args, **kwargs):
                global a
                try:
                    result = example(*args, **kwargs)
                except Exception as exc:
                    print(Fore.LIGHTRED_EX +f"Є, у нас проблема з {exc}, спробуйте вирішити цю проблему"+ Fore.RESET)
                else:
                    if int(result) == result:
                        result = int(result)
                    else:
                        pass
                    print(Fore.BLUE +"Проблем не знайдено, "+ Fore.GREEN +f"Результат = {result}"+ Fore.RESET)
                    c = str(input(Fore.LIGHTGREEN_EX +"Якщо вам потрібно записати в змінну цей результат, виведіть 'rem': "+ Fore.RESET))
                    if c == "rem":
                        a = result
            return checker

        def calculate(expression):
            return eval(expression)

        print("результат має бути приблизно таким "+ Fore.GREEN +"a ** ( 1 / b )"+ Fore.RESET)
        print(Fore.LIGHTMAGENTA_EX +"Example:")
        print(Fore.GREEN +"4 ** ( 1 / 2 ) = 2"+ Fore.RESET)
        print("")

        calculator = checker(calculate)
        test = str(input(Fore.LIGHTGREEN_EX +"Введи свою формулу для обрахунку валюти: "+ Fore.RESET))
        if "a" in test:
            test = str(test.replace('a', f'{a}'))
        calculator(test)



    end = int(input(Fore.MAGENTA +"Напишіть 1, якщо вам потрібен конвертер валют, 2 для простого калькулятора: "+ Fore.RESET))
    print("")
    if end == 0:
        sys.exit()
    if end == 1:
        converter()
    elif end == 2:
        calculator()