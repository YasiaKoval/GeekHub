# 6. Всі ви знаєте таку функцію як < range > . Напишіть свою реалізацію цієї функції.
# P.S. Повинен вертатись генератор.
# P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
# https: // docs.python.org/3/library/stdtypes.html  # range
def my_range(start, stop=None, step=1):

    if stop == None:
        start, stop = 0, start
    if step == 0:
        raise ValueError
    if step > 0:
        if start < stop:
            yield start
            start += step
        else:
            raise ValueError
    elif step < 0:
        if start > stop:
            yield start
            start += step
        else:
            raise ValueError


for rang_num in my_range():
    print(rang_num)
