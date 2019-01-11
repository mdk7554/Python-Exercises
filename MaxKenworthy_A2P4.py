'''
Exercise: Create program that emulates a game of dice that incorporates betting and multiple turns. Include a functional
account balance that is updated with appropriate winnings/losses.
'''

import random

#function to generate a value from dice roll
def roll():
    return int(random.randrange(1,7))

#function to get bet amount as input from user and update balance or exit game
def get_bet(bal):
    while True:
        bet = input("Current balance is ${}. Enter 'x' to exit or place your bet: ".format(bal))
        if bet == 'x':
            return 0,0
        try:    #try/except clause to catch invalid input from user
            bet=int(bet)      
            if bet in range(0,bal+1):
                new_bal=bal-int(bet)
                return bet,new_bal
            else:
                print("Invalid amount. Try again.")
        except ValueError:
            print("Invalid amount. Try again.")
                

#function to control third roll option
def opt_roll(roll_sum,bal,bet):
    while True:
        opt=input("No luck. Do you want to double your bet for a third roll? Enter 1 for yes or 0 for no ")
        try:    #try/except to catch invalid input from user
            opt=int(opt)
            if opt==0:
                return None
            elif bal<bet:
                print('Sorry you dont have enough for this bet.')
                return None
            elif opt==1:
                return roll_sum + roll()
            else:
                print("Invalid entry. Try again.")
        except ValueError:
            print("Invalid entry. Try again.")

#initial balance
bal = 100


while bal>0:    #begin game with while loop that ends when the users balance = 0
    bet,bal = get_bet(bal)  #get input bet from user
    if bet==0 and bal==0:   #exit game if user chooses
        break
    roll1= roll()+roll()
    print('You rolled a {}'.format(roll1))
    if roll1 == 7 or roll1==12:
        print('You win!')
        bal = bal+bet*3
    elif roll1 != 7 and roll!=12:
        roll2 = opt_roll(roll1,bal,bet) #third roll option
        if roll2 == 7 or roll2 == 12:
            print('You rolled a {}'.format(roll2))
            print('You win!')
            bal = bal+bet*4    
        elif roll2==None:  
            pass    #pass and restart loop if user elects not to roll 3rd time
        else:
            print('You rolled a {}'.format(roll2))
            print('Sorry, better luck next time.')
            bal= bal-bet
    else:
        pass
    
print('Thanks for playing. Goodbye!')
