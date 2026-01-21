# WAP to create a dictionary of employee with keys: Employee_ID, name, degn, sal

dict = {}

keys = ['Emp_ID', 'Name', 'Degn', 'Sal']

for key in keys:
    print('Enter', key)
    dict[key] = input()

print(dict)