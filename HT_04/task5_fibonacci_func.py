# 5. Написати функцію fibonacci, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
def fibonacci(fib_num):
    if fib_num == 0:
        return 0
    elif fib_num == 1:
        return 1
    else:
        return fibonacci(fib_num-1)+fibonacci(fib_num-2)


def all_fibonacci(fib_num2):
    printfib = []
    for fibnum in range(0, fib_num2):
        printfib.append(fibonacci(fibnum))
    print(printfib)


all_fibonacci(int(input('Введіть ціле число, яке вище або дорівнює 0:')))
