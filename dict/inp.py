# WAP to create a dict where both the keys and values are user input

dict = {}

while(input('Want to enter?[y/n]:')!='n'):
    key = input('Enter key:')

    print('What is', key, 'str(1), float(2), int(3)?:')
    ch = int(input())

    match ch:
        case 1:
            dict[key] = input('Enter value:')
        
        case 2:
            dict[key] = float(input('Enter value:'))

        case 3:
            dict[key] = int(input('Enter value:'))

print(dict)
