# Number guessing game
import random

print('Number Guessing Game')
cpu = random.randint(1,100)
attempts = 0

print('Rules:\nYou have to guess a number bet. 1 and 100\nYou can exit anytime typing quit\n\nLet\'s begin!\n')

won = False

while True:
    guess = input('Enter your guess:')
    
    if guess=='quit':
        break
    else:
        attempts+=1
        guess = int(guess)
        if cpu==guess:
            won = True
            break

        if cpu-guess>50:
            print('Too low')
        elif cpu-guess>10:
            print('Low')
        elif guess-cpu>50:
            print('Too high')
        elif guess-cpu>10:
            print('High')
        elif cpu-guess<=5 and cpu-guess>=0:
            print('Hint: Think more, You are absolutely Near')
        elif guess-cpu<=5 and guess-cpu>=0:
            print('Hint: Think low. You are absolutely near')
        elif abs(cpu-guess)<=10:
            print('Near')
        
if won == True:
    print(f'\nHooray! Correct Guess')
else:
    print(f'\nYou exited the game')

print(f'CPU:{cpu}\nAttempts:{attempts}')
