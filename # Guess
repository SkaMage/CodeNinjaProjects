import random

code = random.randint(0, 500)
guess = -1
count = 0

while code != guess:
    guess = int(input('Guess a code between 0 - 1000 '))
    count = count + 1
    
    if guess < code:
        print('Too low!')
        
    if guess > code:
        print('Too High')
        
print('You Win!')
print('It took ' + str(count) + ' guesses')
