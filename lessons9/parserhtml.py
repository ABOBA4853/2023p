import requests as r
class ParserHTML:
    def __init__(self, url = ""):
        self.Counter = 0
        self.Result = {}
        self.Url = url
    def ParseCoin(self, separator1 ="", separator2 ="", prefix =""):
        response = r.get(self.Url)
        response_text = response.text
        response_split_list = response_text.split(separator1)#<span>
        for parse_element_1 in response_split_list:
            if parse_element_1.startswith(prefix): #$
                sequence = parse_element_1.split(separator2)#</span>
                for parse_element_2 in sequence:
                    if parse_element_2.startswith(prefix) and parse_element_2[1].isdigit():
                        self.Result[self.Counter] = parse_element_2
                        self.Counter += 1
        self.Counter = 0