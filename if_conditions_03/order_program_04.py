# program to get order discount
# inputs :
item_cost = 500
item_qty = 3
special_client = 1      #  1 : specal       0 : not special

# processing [ program ]
total_order_cost = item_cost * item_qty
if total_order_cost >= 1000:
    if special_client == 1:
        discount_pct = 20
    else:
        discount_pct = 10
else:
        discount_pct = 0

discount_val = discount_pct / 100 * total_order_cost

print('discount pct = ', discount_pct)
print('discount val = ', discount_val)
print('Total before discount = ', total_order_cost)
total_order_cost = total_order_cost - discount_val
print('Total after discount = ', total_order_cost)