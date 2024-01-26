# Ex No. 2 : # List of Dictionaries : create a list of dictionary with student id as key and name as value
# 1 dict,       1 element in the list
persons_list = [  { 101:'Farouk', 102: 'Marwa', 103:'Mostafa' }   ]
print(persons_list) # print whole List
print( persons_list[0] )    # print dict { 101:'Farouk', 102: 'Marwa', 103:'Mostafa' }

print( persons_list[0][102] ) # Marwa
persons_list[0][102] = 'Marwa Mahmoud' # edit Marwa > Marwa Mahmoud
print(persons_list)
print('------------- Adding second dict to the list --------------')
dict2 = {104: 'Ibrahim', 105: 'Usama'}
persons_list.append(dict2)      # adding dict 2 as a new element in the list
print(persons_list[1])
persons_list[1][105] = 'Usama Khalil'   # modify key 105 in dict 2 in the list
persons_list[1][106] = 'Ehab'   # adding new employee to dict 2 in the list
print(persons_list[1])



