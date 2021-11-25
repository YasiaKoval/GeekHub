# 7. Ну і традиційно -> калькулятор: ) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
def calculus(num1, num2, operation):
    if operation == '+':
        print('Результат додавання: ', num1+num2)
    elif operation == '-':
        print('Результат віднімання: ', num1-num2)
    elif operation == '/':
        print('Результат ділення: ', num1/num2)
    elif operation == '*':
        print('Результат множення: ', num1*num2)
    elif operation == '//':
        print('Результат ділення націло: ', num1//num2)
    elif operation == '%':
        print('Остача після ділення: ', num1 % num2)
    elif operation == '^' or operation == '**':
        print('Результат піднесення до степеня: ', num1**num2)
    else:
        print('Така операція не виконується.')


calculus(float(input('Введіть 1-ше число: ')),
         float(input('Введіть 2-ге число: ')), input('Введіть знак операції: '))
