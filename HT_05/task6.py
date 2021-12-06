# 6. Всі ви знаєте таку функцію як < range > . Напишіть свою реалізацію цієї функції.
# P.S. Повинен вертатись генератор.
# P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
# https: // docs.python.org/3/library/stdtypes.html  # range
def my_range(start, stop=None, step=1):
    if stop == None:
        start, stop = 0, step
    if step == 0:
        raise ValueError
    if step > 0:
        while True:
            yield start
            start += step
    elif step < 0:
        while True:
            yield start
            start += step


for rang_num in my_range():
    print(rang_num)
