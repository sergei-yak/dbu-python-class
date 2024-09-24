#Directions: Create a Rock, Paper, Scissors game that allows the user to play against the computer. The program should prompt the user to enter their choice, then randomly select a choice for the computer. The program should then determine the winner and print the result. The program should continue to play until the user chooses to exit.
#The program should have the following functions:
#Requiements: Save the functions in a separate file called groupex.py and import them into the main program.

#Function to get user input
#Request User Input

def user_input_function():
    choices = ["rock", "scissors", "paper", 'exit']
    user_input = input('Type one of the options (rock, scissor or paper): ')
    if user_input in choices:
        return user_input
    else:
        return 'Invalid choice'
#Validate User Input using IN operator and LIST
#Return User Input

#Function to get computer's choice
import random
def comp_input_function():
    choices = ["rock", "scissors", "paper"]
    return random.choice(choices)
#Create a list of choices
#Return a random choice from the list
#To use random choices, import random module, and use random.choice() method

#Function to determine the winner
#Compare user's choice and computer's choice
def winner_func(user, comp):
    if user == comp:
        return "It's a tie!"
    elif user == 'rock' and comp == 'scissors':
        return "You win!"
    elif user == 'paper' and comp == 'rock':
        return "You win!"
    elif user == 'scissors' and comp == 'paper':
        return "You win!"
    elif user == 'exit':
        return 'Exit'
    else:
        return "Computer wins!"
#IF both choices are the same
    #Return "It's a tie!"
#ELSE IF user's choice is rock and computer's choice is scissors
    #Return "You win!"
#ELSE IF user's choice is paper and computer's choice is rock
    #Return "You win!"
#ELSE IF user's choice is scissors and computer's choice is paper
    #Return "You win!"
#ELSE IF user's choice is exit
    #Return "exit"
#ELSE
    #Return "Computer wins!"

#START main
gameOn = True
#PRINT welcome message
print('Hello...')
while gameOn:
    #CALL a function to get user input and store the result as a variable (user_choice)
    user_choice = user_input_function()
    if user_choice == 'exit':
        gameOn = False
        print('Thanks for playing')
        break
    #CALL a function to get computer's choice and store the result as variable (computer_choice)
    computer_choice = comp_input_function()
    #PRINT both user and computer choices
    print('User input: ', user_choice)
    print('Computer input: ', computer_choice)
    #CALL a function to decide the winner between two choises (user_choice and computer_choice)
    w = winner_func(user_choice, computer_choice)
    #PRINT the result of the game
    print(w)
    #LOOP until the game is over with the user's choice
    #END main

#test for github push