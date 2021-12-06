# 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
#   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр
# < silent > (значення за замовчуванням - <False > ). Логіка наступна:
# якщо введено коректну пару ім'я/пароль - вертається < True >
# якщо введено неправильну пару ім'я/пароль і < silent > == < True > - функція вертає < False >,
# інакше ( < silent > == < False > ) - породжується виключення LoginException
class LoginException(Exception):
    pass


def user(name, password, silent=False):
    func_users = [['Anna', 47743], ['Scott', 36011],
                  ['Alexander', 41384], ['Diaonisys', 51407]]
    try:
        if [name, password] in func_users:
            silent = True
        else:
            if [name, password] in func_users == False and silent == True:
                silent = False
            elif [name, password] in func_users == False and silent == False:
                raise LoginException()
    except LoginException:
        print("Ваше ім'я та пароль не занесено в нашу базу данних")
    else:
        return silent


print(user(input("Введіть ваше ім'я (англ): "), int(input('Введіть ваш пароль: '))))
