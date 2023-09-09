from docontext import DBContext
context = DBContext("exam.sl3")
records_to_insert = [
    (1, 'https://bank.gov.ua/', 'nbu'),
    (2, 'https://ua.sinoptik.ua/погода-святопетрівське', 'weather')
]
query = "INSERT INTO LINKS (id, link, name) VALUES(?, ?, ?)"
context.QueryMany(query, records_to_insert)


