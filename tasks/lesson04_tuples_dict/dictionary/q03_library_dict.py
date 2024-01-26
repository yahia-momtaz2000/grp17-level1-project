# Adding new element ( author ) To a Dictionary
# Accessing Elements ( name ) inside a Dictionary
# Changing Elements inside a Dictionary year to 2010
# Use Loop to print keys and values
# Removing Item ( name ) from a Dictionary

book_dict = {'pages': 277, 'name':'Gone Girl', 'year': 2007 }
print('Original = ', book_dict)
book_dict['Author'] = 'Well Max'
print('After adding author ', book_dict)
print('Book name = ', book_dict['name'])
book_dict['year'] = 2008
print('After Change element year to 2008 : ', book_dict)
print('Loop to print keys and values')
for key, value in book_dict.items():
    print(key, value)
print('Remove item from a dictionary')
book_dict.pop('name')
print(book_dict)