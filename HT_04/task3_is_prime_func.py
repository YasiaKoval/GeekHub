# 3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
# і яка вертатиме True, якщо це число просте, і False - якщо ні.
def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for count in range(2, number):
            if number % count == 0:
                return False
        return True


print(is_prime(int(input('Введіть ціле число від 0 до 1000: '))))
