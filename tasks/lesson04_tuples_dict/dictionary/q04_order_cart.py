# loop over all keys and raise the prices 10%
# Print sum of all the values after raise 10%
# Add vat 14$ to the total and print the net value
shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}

print('Original Dict : ', shopping_cart_dict)
# raise values by 10% and Solve total order
total_order = 0
for item, value in shopping_cart_dict.items():
    shopping_cart_dict[item] = value + value * 0.1
    total_order = total_order + shopping_cart_dict[item]

print('After 10% raise : ', shopping_cart_dict)
print('Total order : ', total_order)

# solve Vat 14%
order_net_salary = total_order + total_order * 0.14
print('After vat - net salary = ', order_net_salary)
