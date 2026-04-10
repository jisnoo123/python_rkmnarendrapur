un_pw = {}

n = int(input('Enter no. of users:'))

# Input
for i in range(n):
    user_name = input(f'Enter username_{i}: ')
    password = input(f'Enter password: ')
    un_pw[user_name] = password

# Login
print("Enter login credentials")
user_name = input('Enter User Name:')
attempts = 0
broke = False

while attempts<5:
    password = input('Enter password:')
    attempts += 1
    if password == un_pw[user_name]:
        broke = True
        break
    else:
        print(f'Incorrect password! {5-attempts} attempts left')

if broke == True:
    print('\nWelcome! You are logged in')
else:
    print('\nStay out imposter!')
