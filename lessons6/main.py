'''
try:
    your_code
except type_of_Exception:
    your_code
except ......
'''
'''
while(True):
    try:
        digit1 = int(input('Enter digit1: '))
        digit2 = int(input('Enter digit2: '))
        print(digit1/digit2)
        yes = input('Do you want try again [Y/N]?: ')
        if (yes.lower() != 'y'):
            break

    except ZeroDivisionError as zde:
        print(f'Standart exception {zde}')
        yes = input('You have to enter value not equal 0 for digit2\n'
                    'Do you want try again [Y/N]?: ')
        if (yes.lower() != 'y'):
            break
    except Exception as ex:
        print(f'Standart exception {ex}')
        yes = input('You have to enter right value as digit(int)\n'
                    'Do you want try again [Y/N]?: ')
        if(yes.lower() != 'y'):
            break
'''
from limiterror import LimitError
from validation import Checker
checker = Checker()
try:
    amount = int(input("Enter digit1: "))
    limit = 5
    if(checker.Check(amount, limit)):
        print("Your order proccessed successful!")
except LimitError as le:
    print(le)
except ValueError as ve:
    print(ve)


