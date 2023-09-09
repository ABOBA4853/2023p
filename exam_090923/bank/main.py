
from parsehtml import ParserHTLM
selectedCurrency = int(input("Select currency: \n[EU - 1]\n[USD - 2]: "))
amount = float(input("Enter amount in hrn: "))
parser = ParserHTLM("https://bank.gov.ua/")
isUSD = True
symbol = "$"
if selectedCurrency == 1:
    isUSD = False
    symbol = "€"
parser.ParseNBU('value-full', 'small', isUSD)
result = amount / parser.Result[0]
print(f"amount - {amount} hrn\n"
      f"price - {parser.Result[0]} {symbol}\n"
      f"result - {result:.2f} {symbol}")