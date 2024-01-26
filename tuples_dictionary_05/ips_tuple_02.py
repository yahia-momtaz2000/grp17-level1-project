# program to show a List of Tuples
ips_list = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.81', 'n'),
    ('192.168.0.11', 'y')
]
print(ips_list)

print('----- second element from the list index 1  ----')
print( ips_list[1] )
print('-------   second element from the list index 1, y or no ----')
print( ips_list[1][1] )
print('---------- print all ips that are Y ---------')
for i in range(  len(ips_list)  ):
    if ips_list[i][1] == 'y':
        print(ips_list[i], ips_list[i][0][ -2 : ] )
        
# task : print the last part of the yes ip in the last loop
"""
('192.168.0.15', 'y')   15
('192.168.0.22', 'y')   22
('192.168.0.14', 'y')   14
('192.168.0.11', 'y')   11
"""




