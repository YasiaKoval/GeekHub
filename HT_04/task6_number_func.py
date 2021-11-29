# 6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
def number_func(number):
    if number > 0:
        return number**2
    elif number < 0:
        return number+100
    elif number == 0:
        return number


print(number_func(int(input('Введіть ціле число: '))))
