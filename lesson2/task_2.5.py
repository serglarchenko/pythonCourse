import os

from prettytable import PrettyTable

path = r'C:\Users\Serhii_Larchenko\Desktop\ORKE\\'
dirs = os.listdir(path)
stats = os.stat(path)
print(f'List dir {dirs}')

table = PrettyTable()
table.field_names = ['Mode', 'Owner', 'Group', 'Size', 'File name']

for file in dirs:
    table.add_row([os.stat(path + file).st_mode, os.stat(path + file).st_uid, os.stat(path + file).st_gid,
                   os.stat(path + file).st_size, file])

print(table)
