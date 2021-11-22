dict_1 = {1: 10, 2: 20}
dict_2 = {3: 30, 4: 40}
dict_3 = {5: 50, 6: 60}
for general_dict in (dict_2, dict_3):
    dict_1.update(general_dict)
print(dict_1)
