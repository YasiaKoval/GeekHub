# 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
# і вертатиме список простих чисел всередині цього діапазона.
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


def prime_list(start, end):
    list_prime_num = []
    for numbers in range(start, end+1):
        if is_prime(numbers) == True:
            list_prime_num.append(numbers)
    return list_prime_num


print(prime_list(int(input('Введіть початок діапазона: ')),
      int(input('Введіть кінець діапазона: '))))
