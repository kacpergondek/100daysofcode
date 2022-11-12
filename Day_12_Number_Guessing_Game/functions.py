import random
from assets import *
# Main game loop
def main():
    print(logo + "\nI'm thinking of a number between 1 and 100")
    difficulty_level = input("\nChoose a difficulty. Type easy or hard ").lower()
    lifes = initialize_lifes(difficulty_level)
    random_number = random.choice(number_list)
    # While you have lifes, check user inputs and search for "end" to end the game
    while lifes >= 0:
        print (f"You have {lifes} attempts to guess the number")
        guess = input("Make a guess: ")
        x = checkPlayerGuess(guess,random_number)
        if x == "end":
            exit()
        lifes -= x




# Add lifes depending on the difficulty
def initialize_lifes(difficulty_level):
    global lifes
    if difficulty_level == 'e' or difficulty_level == 'easy':
        print("You have selected easy difficulty")
        return 10    
    elif difficulty_level == 'h' or difficulty_level == 'hard':
        print("You have selected hard difficulty")
        return 5
    else:
        print("Cannot understand your input, defaulting to easy")
        return 10

#Check the input provided by player and provide information needed  
def checkPlayerGuess(num,ans):
    global lifes
    number = int(num)
    answer = int(ans)
    if number == answer:
        print(f"Congrats, the number was in fact {answer}")
        return "end"
    elif lifes <= 0:
        print(f"The number was {answer}. You lose.") 
        return "end"
    elif number > 100:
        print("The number you entered is above the range I've mentioned.\nYou lose a life for that as well")
        return 1
    elif number > answer:
        print("The number is too high, try again")
        return 1
    elif number < answer:
        print("The number is too low, try again")
        return 1

        
