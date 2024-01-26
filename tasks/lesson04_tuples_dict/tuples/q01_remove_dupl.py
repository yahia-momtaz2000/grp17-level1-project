# Remove Duplicates From a List of Tuples : Make it unique List
ips_List = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.15', 'y'),
    ('192.168.0.11', 'y')
]
unique_list = []
for ip in ips_List:
    if ip not in unique_list:
        unique_list.append(ip)

print(unique_list)