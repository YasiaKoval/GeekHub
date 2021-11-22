number_amount = int(input("Введіть ціле позитивне число: "))
square_dict = {}
for numam in range(number_amount+1):
    square_dict[numam] = numam**2
print(square_dict)
