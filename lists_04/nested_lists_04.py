# program to show nested lists
my_nested_list = [[101, 'ahmed', 'Cairo'], [102, 'mostafa', 'Alex']]
print(my_nested_list)
print(my_nested_list[0]) # [101, 'ahmed', 'Cairo']
print(my_nested_list[0][2]) # cairo

my_nested_list = \
    [[101, 'ahmed', ['Cairo', 'Nasr city', 'Makram ebeid']], [102, 'mostafa', 'Alex']]
print(my_nested_list[0][2][2]) # Makram Ebied

