print ('ПРИВІТ ТИ У КАЛЬКУЛЯТОРІ Python')
q1 = int (вхід('Введіть число 1: '))
q2 = int (вхід('Введіть число 2: '))

v = int (input('Яку операцію ви хочете виконати? \n 1 додавання \n 2 віднімання \n 3 ділення \n 4 множення \n'))

if v == 1:
    r = q1 + q2
    p = 'додавання'
    t = p
if v == 2:
    r = q1 - q2
    l = 'віднімання'
    t = l
if v == 3:
    r = float(q1 / q2)
    m = 'ділення'
    t = m
if v == 4:
    r = q1 * q2
    n = 'множення'
    t = n
print ('Результат ',t,' = ',r)