# Converting a List of Tuples to a Dictionary
colors_list = [ ('red', 223 ), ('blue', 201 ), ('green', 210 ) ]

colors_dict = {}
for color in colors_list:
    colors_dict[color[0]] = color[1]

print(colors_dict)