# program to show dictionary operations
print('---- create and print dictionary -----')
shopping_cart_dict = {'Milk': 30.0, 'Eggs': 140.0, 'Bread': 10.0}
print(shopping_cart_dict)
print(type(shopping_cart_dict))

print('------ Adding, change new pair to the dictionary -------')
shopping_cart_dict['Nescafe'] = 20.0 # adding
shopping_cart_dict['Milk'] = 40.0 # Editing
print(shopping_cart_dict)

print('------ access element -----')
print('price of Nescafe = ', shopping_cart_dict['Nescafe'] )

print('---- delete element pair from dict ------')
shopping_cart_dict.pop('Milk') # removing by key
print(shopping_cart_dict)