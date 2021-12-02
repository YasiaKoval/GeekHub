# 5. Запишіть в один рядок генератор списку(числа в діапазоні від 0 до 100), сума цифр кожного елемент якого буде дорівнювати 10.
# Перевірка: [19, 28, 37, 46, 55, 64, 73, 82, 91]
#gen_list = [number1 for number1 in range(100) for dig in number1 if dig[0]+dig[1] == 10]
gen_list = []
for number1 in range(100):
    for dig in str(number1):
        if int(dig[0])+int(dig[1]) == 10:
            gen_list.append
        else:
            None
