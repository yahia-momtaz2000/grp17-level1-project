# Ex No. 3 : # Combine two different dictionaries and plus same keys
dict1 = {'a': 100, 'b': 150, 'c': 100}
dict2 = {'a': 50, 'c': 100, 'd': 150}

# solution :   dict1 = {'a':150, 'b': 150, 'c': 200, 'd': 150 }
# 1. loop over dict 2 : to catch any differ keys
for key, value in dict2.items():
    if key in dict1:  # ( add ) value of key
        dict1[key] = dict1[key] + value    # 100 + 50
    else:           # Add k, v to dict 1
        dict1[key] = value             # dict1['d'] = 150

print(dict1)