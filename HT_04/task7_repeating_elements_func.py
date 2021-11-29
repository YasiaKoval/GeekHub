# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
def count_el(given_list):
    print(dict((repeated_num, given_list.count(repeated_num))
          for repeated_num in set(given_list)))


count_el(list(input('Введіть елементи списку без пропуску: ')))
