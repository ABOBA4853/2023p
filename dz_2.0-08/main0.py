class Expression:
    def interpret(self, num1, num2):
        pass

class Addition(Expression):
    def interpret(self, num1, num2):
        return num1 + num2

class Subtraction(Expression):
    def interpret(self, num1, num2):
        return num1 - num2

class Multiplication(Expression):
    def interpret(self, num1, num2):
        return num1 * num2

class Division(Expression):
    def interpret(self, num1, num2):
        return num1 / num2

class Power(Expression):
    def interpret(self, num1, num2):
        return num1 ** num2


def calculate(expression):
    tokens = expression.split()
    num1 = int(tokens[1])
    num2 = int(tokens[2])

    if tokens[0] == "додати":
        return Addition().interpret(num1, num2)
    elif tokens[0] == "відняти":
        return Subtraction().interpret(num1, num2)
    elif tokens[0] == "множити":
        return Multiplication().interpret(num1, num2)
    elif tokens[0] == "ділити":
        return Division().interpret(num1, num2)
    elif tokens[0] == "піднести до степеню":
        return Power().interpret(num1, num2)
    else:
        return None

while True:
    print("КАЛЬКУЛЯТОР")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Піднесення до степеня")
    print("0. ВИХІД")
    choice = int(input("Виберіть варіант: "))
    if choice == 0:
        break
    num1 = int(input("Введіть перше число: "))
    num2 = int(input("Введіть друге число: "))
    if choice == 1:
        result = calculate("+ " + str(num1) + " " + str(num2))
        print("Результат: ", result)
        break
    elif choice == 2:
        result = calculate("- " + str(num1) + " " + str(num2))
        print("Результат: ", result)
        break
    elif choice == 3:
        result = calculate("* " + str(num1) + " " + str(num2))
        print("Результат: ", result)
        break
    elif choice == 4:
        result = calculate("/ " + str(num1) + " " + str(num2))
        print("Результат: ", result)
        break
    elif choice == 5:
        result = calculate("^ " + str(num1) + " " + str(num2))
        print("Результат: ", result)
        break
    else:
        print("Невірний вибір.")