import random

yourchoice = int(input('Rock(1), Paper(2), Scissors(3)! '))

computer = random.randint(1,3)

if yourchoice == computer:
    print('Tie! ')
else:
    if yourchoice == 1:
        if computer == 2:
            print('You Lose! Maybe next time my dude ')
        else:
            print('Congrats! You Win! Cheater...' )
        
    if yourchoice == 2:
        if computer == 3:
            print('You Lose! Maybe next time my dude ')
        else:
            print('Congrats! You Win! Cheater...')
            
    if yourchoice == 3:
        if computer == 1:
            print('You Lose! Maybe next time my dude ')
        else:
            print('Congrats! You Win! Cheater...')
            
print('The opponent chose ' + str(computer))
