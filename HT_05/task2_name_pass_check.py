'''2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
 - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
 - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
 - щось своє: )
 Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.'''


class NameException(Exception):
    pass


class PassException(Exception):
    pass


class NameException2(Exception):
    pass


def check_func(name, password):
    if len(name) <= 3 or len(name) > 50:
        raise NameException("Ім'я має бути довше трьох літер та менше 50!!!")
    for symbol in password:
        if symbol.isdigit():
            pass_con = True
    if len(password) < 8 or pass_con == False:
        raise PassException(
            "Пароль повинен мати мінімум 8 символів і одну цифру!")
    if name.istitle() == False:
        raise NameException2("Ім'я має писатися з великої літери!")


check_func(input("Введіть ваше ім'я: "), input("Введіть вам пароль: "))
