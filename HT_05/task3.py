'''3. На основі попередньої функції створити наступний кусок кода:
 а) створити список із парами ім'я/пароль різноманітних видів(орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
 б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані
 і надрукує для кожної пари значень відповідне повідомлення, наприклад:
 Name: vasya
 Password: wasd
 Status: password must have at least one digit
 - ----
 Name: vasya
 Password: vasyapupkin2000
 Status: OK
 P.S. Не забудьте використати блок try/except; )'''
data = [['Anna', 'anna'], ['Scott', 'scott360'], [
    'alexander', 'alex4138'], ['Diaonisys', 'diaon1']]


class NameException(Exception):
    pass


class PassException(Exception):
    pass


class NameException2(Exception):
    pass


def check_func(name, password):
    status = ''
    try:
        if len(name) <= 3 or len(name) > 50:
            raise NameException(
                "Ім'я має бути довше трьох літер та менше 50!!!")
        for symbol in password:
            if symbol.isdigit():
                pass_con = True
        if len(password) < 8 or pass_con == False:
            raise PassException(
                "Пароль повинен мати мінімум 8 символів і одну цифру!")
        if name.istitle() == False:
            raise NameException2("Ім'я має писатися з великої літери!")
    except NameException as error:
        status = error
    except PassException as error:
        status = error
    except NameException2 as error:
        status = error
    else:
        status = "OK"
    return status


for number in range(len(data)):
    checked_status = check_func(data[number][0], data[number][1])
    print(f'Name: {data[number][0]}')
    print(f'Password: {data[number][1]}')
    print(f'Status: {checked_status}')
