tuplist = [(30, 420, 55), (96, 87, 54), (123, 456, 789)]
changed_number = int(input("Введіть ціле число, на яке бажаєте змінити останні числа елементів списку: "))
print([tups[:-1] + (changed_number,) for tups in tuplist])
