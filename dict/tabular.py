# WAP to crate a list of n students and print the result in tabular form

fields = list()

while(input('Enter field?[y/n]:')!='n-'):
    fields.append(input())


db = list()

# Input

while(input('Enter student details?[y/n]')!='n'):
    dict = {}
    for field in fields:
        print('Enter', field, ':')
        match field:
            case 'Roll':
                dict[field] = int(input())
            
            case 'Name' | 'College':
                dict[field] = input()

            case 'Marks':
                dict[field ] = input()
    list.append(dict)

# Display
for field in fields:
    print(field,'\t\t', end='')

print()

for i in range(len(db)):
    for field in fields:
        print(db[i][field],'\t\t', end='')
    print()
