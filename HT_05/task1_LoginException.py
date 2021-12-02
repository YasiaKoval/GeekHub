# 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
#   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр
# < silent > (значення за замовчуванням - <False > ). Логіка наступна:
# якщо введено коректну пару ім'я/пароль - вертається < True >
# якщо введено неправильну пару ім'я/пароль і < silent > == < True > - функція вертає < False >,
# інакше ( < silent > == < False > ) - породжується виключення LoginException
class LoginException(Exception):
    pass


def user(name, password, silent=False):
    func_users = [['Anna', 47743, False], ['Scott', 36011, False],
                  ['Alexander', 41384, False], ['Diaonisys', 51407, False]]
    if [name, password, silent] in func_users == True:
        return True
    elif [name, password, silent] in func_users == False and silent == True:
        return False
    elif [name, password, silent] in func_users == False and silent == False:
        raise LoginException(
            "Ваше ім'я та пароль не занесено в нашу базу данних")


user(input("Введіть ваше ім'я (англ): "), int(input('Введіть ваш пароль: ')))
print(user)
