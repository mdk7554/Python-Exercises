## Max Kenworthy
## 9/24/18
## honor statement "I have not given or received unauthorized assistance on this assignment"

# P4

def game():
    name = input('Please enter name: ')
    print('Hello '+name+", welcome to the word game! The rules are simple: change the starting word to the goal word in as few steps as possible by inserting, removing, or replacing cahracters one by one. Your starting word is 'book' and the goal word is 'tool'.")
    word='book'
    step=0
    while word != 'tool':
        option = input("Enter 'a' to insert a character, 'b' to remove character, or 'c' to replace a character.")
        if option == 'a':
            a_char = input('Input character to insert: ')
            a_ind = int(input('Input index where to insert character: '))
            word = word[:a_ind] + a_char + word[a_ind:]   #split word apart by index and insert character given by user
            step += 1  #update step count
            print('Step #'+ str(step) +'  '+ word)  #print word after change and current step count
        elif option == 'b':
            b_ind = int(input('Input index of letter to be removed: '))
            word = word[:b_ind-1] + word[b_ind:]  #delete character at index given by user and update word
            step += 1
            print('Step #'+ str(step) +'  '+ word)
        elif option == 'c':
            c_ind = int(input('Input index of character to be replaced: '))
            c_char = input('Input character to replace: ')
            word = word[:c_ind-1] + c_char + word[c_ind:]  #delete and insert character at index given by user
            step += 1
            print('Step #'+ str(step) +'  '+ word)
        else:
            print('Invalid option. Choose a, b, or c.')
    print("Congratulations "+name+"! It only took you "+str(step)+" steps")  #print statement when goal word reached

game()  #initiate game function



#sample run:

#>>> game()
#>Please enter name: max
#>Hello f, welcome to the word game! The rules are simple: change the starting word to the goal word in as fewsteps as possible by inserting, removing, or replacing cahracters one by one. Your starting word is BOOK andthe goal word is TOOL.
#>Enter 'a' to insert a character, 'b' to remove character, or 'c' to replace a character.c
#>Input index of character to be replaced: 1
#>Input character to replace: t
#>Step #1  took
#>Enter 'a' to insert a character, 'b' to remove character, or 'c' to replace a character.c
#>Input index of character to be replaced: 4
#>Input character to replace: l
#>Step #2  tool
#>Congratulations max! It only took you 2 steps
