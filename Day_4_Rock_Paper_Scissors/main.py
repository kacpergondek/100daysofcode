import random 
import graphics

playerinput = int(input('Welcome to the game. Please pick \n0 for rock, \n1 for paper, \n2 for scissors.\n'))

number = random.randint(0,2)

choice = [graphics.rock,graphics.paper,graphics.scissors]
text = ["You have lost","You have won","It's a draw"]
playerchoice = choice[playerinput]
computerchoice = choice[number]

final = ("")

# Rock < Paper < Scissors < Rock

if playerchoice == choice[0] and computerchoice == choice[1]:
    final = text[0]
elif playerchoice == choice[1] and computerchoice == choice[2]:
    final = text[0]
elif playerchoice == choice[2] and computerchoice == choice[0]:
    final = text[0]
elif playerchoice == computerchoice:
    final = text[2]
else:
    final = text[1]

print("You have chosen:\n\n")
print(playerchoice)
print("Whilst the computer has chosen:\n\n")
print(computerchoice)
print(final)