#Guessing The Number Game
#\n and print() are used in different lines for better view of output
#this firse while loop for repeating game.
while True:
    print('\n_________GUESSING THE NUMBER GAME_________\n')
    print('Welcome In A Guessing The Number Game...')
    print('Lets GO...')
    print('Think Any Number From 1 To 100...')
    print("Answer The Question By 'Y' or 'y' For YES and 'N' or 'n' For NO...")
    input('Press ENTER When You Are Ready...')
    print('So Lets Start...\n\n')
    #algorithm starts from here
    low=1
    high=100
    #this second while loop for executing algorithm
    while low<=high:
        mid=int((low+high)/2)
        print('Is Your Number',mid,'?',end=('_____'))
        Q1=input(' ')
        print()
        if Q1=='Y' or Q1=='y':
            print('Your Choosen Number Is',mid)
            break
        if Q1=='N' or Q1=='n':
	    #this is third while loop
            while True:
                print('Then Greater Than',mid,'?',end='____')
                Q2=input(' ')
                print()
                if Q2=='Y' or Q2=='y':
                    low=mid+1
                    break
                elif Q2=='N' or Q2=='n':
                    high=mid-1
                    break
                else:
                    print('Please Enter Valid Answer According To Given Instruction...\n')
	#this else is of if ,when user enter invalid input
        else:
            print('Please Enter Valid Answer According To Given Instruction...\n')
    #this else is of first while loop and then executes when user did any mistake
    else:
        print('\nEither You Have Done Any Mistake or You Are Cheating\n')
    #asked user for playing game again
    again=input("\nIf You Want To Play Again Press 'y' or 'Y'_____ ")
    if again!='y' and again!='Y':
        break
print('\nThanks For Playing Game')
print('Have A Good Day')
print('Good Bye and Take care')
