# 6. Маємо рядок - -> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koi..." -> просто потицяв по клавi
# Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр(лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя
def strfunc(entstr):
    numbers = '0123456789'
    numsum = 0
    symsum = 0
    symsum1 = ''
    if 30 <= len(entstr) <= 50:
        print(f'Довжина рядку: {len(entstr)}')
        for symb in entstr:
            if symb in numbers:
                numsum += 1
            else:
                symsum += 1
        print(f'Кількість цифр: {numsum} та букв: {symsum}')
    elif 30 >= len(entstr):
        for symb in entstr:
            if symb in numbers:
                numsum += int(symb)
            else:
                symsum1 += symb
        print(f'Сума всіх чисел: {numsum}\n{symsum1}')
    elif 50 <= len(entstr):
        for symb in entstr:
            if symb in numbers:
                numsum *= int(symb)
            else:
                symsum1 += symb
        print(f'Добуток усіх чисел: {numsum} \n{symsum1.upper()}')


strfunc(input('Введіть рядок: '))
