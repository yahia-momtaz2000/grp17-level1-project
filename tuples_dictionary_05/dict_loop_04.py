# loop over a dictionary
shopping_cart_dict = {'Milk': 30.0, 'Eggs': 140.0, 'Bread': 10.0}

print('-------- 1. Loop over a dict using For each Loop on Keys -----')
for key in shopping_cart_dict:
    print(key, shopping_cart_dict[key])

print('----------2. Loop over a dict using for each Loop on Keys, Values ----')
for key, value in shopping_cart_dict.items():
    print(key, value)