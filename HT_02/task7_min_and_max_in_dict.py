ex_dict = {'1': 548, '2': 28, '3': 219}
key_max = max(ex_dict.keys(), key=lambda ex_key: ex_dict[ex_key])
key_min = min(ex_dict.keys(), key=lambda ex_key: ex_dict[ex_key])
print("Максимальне значення словника:", ex_dict[key_max],
      "\nМінімальне значення словника:", ex_dict[key_min])
