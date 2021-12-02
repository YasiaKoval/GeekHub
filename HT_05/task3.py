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
    'Alexander', 'alex4138'], ['Diaonisys', 'diaon514']]


class NameException(Exception):
    pass


class PassException(Exception):
    pass


class NameException2(Exception):
    pass


def check_func(name, password):
     if len(name) < 3 or len(name) > 50:
        raise NameException(
            "Ім'я має бути довше трьох літер та менше 50!!!")
     for symbol in password:
         if symbol.isdigit():
            pass_con = True
         else:
             pass_con = False
     if len(password) < 8 or pass_con == False:
        raise PassException(
            "Пароль повинен мати мінімум 8 символів і одну цифру!")
     if name.istitle() == True:
        raise NameException2("Ім'я має писатися з великої літери!")
