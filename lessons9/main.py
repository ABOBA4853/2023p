#1
'''
import urllib.request
opener = urllib.request.build_opener()
response = opener.open("https://httpbin.org/get")
print(response.read())
'''
#2
'''
import requests
response = requests.get("https://httpbin.org/get")
print(response.content)
'''
from parserhtml import ParserHTML
parser = ParserHTML("https://coinmarketcap.com/")
parser.ParseCoin("<span>", "</span>", "$")
print(parser.Result)