import random
from subprocess import call
from os import system, name
import time


cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "Ace"]


mainart = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   <
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_/
                       _/ |                
                      |__/         
 '''

#Clears the screen
def clear():
    _ = call('clear' if name == 'posix' else 'cls')

# Main game function
def main():
    player_cards = []

    dealer_cards = []
    '''Main game loop'''

    clear()
    print(mainart)
    choice = input("Would you like to play a game of Blackjack? (Y)es or (n)o?").lower()
    if choice == 'n' or choice == 'no':
        print("Ok")
        exit()

    # Main Game
 
    elif choice == 'y' or choice == 'yes':

        # We give the player 2 cards, and the dealer as many cards as it takes to reach 17 and more.
        player_cards.append(randomCard(cards))
        player_cards.append(randomCard(cards)) 
        while True:
            if checkTotalPoints(dealer_cards) >= 17:
                break
            elif checkTotalPoints(dealer_cards) < 17:
                x = dealer_cards.append(randomDealerCard(cards))

        # We calculate the score and print it, as well as show first card of the dealer
        score = checkTotalPoints(player_cards)
        print (printPlayerCards(player_cards, score))
        print(f"The dealers' card is {dealer_cards[0]}")

        #The game is running, you can either draw cards or stop

        while True:
            drawornot = input ("Would you like to (s)top taking cards,\nor (d)raw another card?").lower()
            if drawornot == 'd' or drawornot == 'draw':
                clear()
                card_picked = randomCard(cards)
                player_cards.append(card_picked)
                print (f"You have picked{card_picked}")
                score = checkTotalPoints(player_cards)
                print(printPlayerCards(player_cards, score))
                print(f"The dealers' card is {dealer_cards[0]}")

                #If you go over 21, game over

                if score > 21:
                    print ("You went over 21, and therefore you lose.\nYou will now be sent back to the main menu")
                    player_cards = []
                    dealer_cards = []
                    time.sleep(5)
                    main()

            # Drawing cards is finished, it is now time to calculate the results

            elif drawornot == 's' or drawornot == 'stop':
                player_score, dealer_score = checkVictoryCondition(player_cards, dealer_cards)
                if player_score < 22 :
                    if dealer_score > 21:
                        print (f"You won, as the dealer went over 21, accumulating {dealer_score} points")
                        print ("You will now be sent to the main menu.")
                        player_cards = []
                        dealer_cards = []
                        time.sleep(5)
                        main()
                    elif player_score > dealer_score:
                        print (f"Congratulations, you have won with {player_score}, when the dealers score was {dealer_score}")
                        print ("You will now be sent to the main menu.")
                        player_cards = []
                        dealer_cards = []
                        time.sleep(5)
                        main()
                    elif player_score == dealer_score:
                        print (f"It is a draw between you and the dealer, as both of you have {player_score}")
                        print ("You will now be sent to the main menu.")
                        player_cards = []
                        dealer_cards = []
                        time.sleep(5)
                        main()
                    else:
                        print (f"You lost, as the dealer has {dealer_score}, whilst you have {player_score}")
                        print ("You will now be sent to the main menu.")
                        player_cards = []
                        dealer_cards = []
                        time.sleep(5)
                        main()
                else:
                    print(f"You went over 21, and therefore you lose.")
                    print ("You will now be sent to the main menu.")
                    player_cards = []
                    dealer_cards = []
                    time.sleep(5)
                    main()
    else:
        print("Wrong input")
        main()

#Picks a random card from cards list, and returns it.

def randomCard(cards):
    card = random.choice(cards)
    if card == "Ace":
        card = selectAce(card)
    return int(card)

#Picks a random card for the dealer.

def randomDealerCard(cards):
    card = random.choice(cards)
    if card == "Ace":
        if checkTotalPoints(cards) < 10:
            dealer_cards.append(11)
        else:
            dealer_cards.append(1)
    return int(card)


# Checks for >21 points in each player

def checkVictoryCondition(deck1, deck2):
    player_score = checkTotalPoints(deck1)
    dealer_score = checkTotalPoints(deck2)
    return player_score,dealer_score

#Calculates total score for a deck of cards

def checkTotalPoints(deck):
    total = 0
    for card in deck:
        total += card
    return total

#Prints the cards that the player has in their hand

def printPlayerCards(deck, score):
    return f"Your cards are {deck}, with total score: {score}"

#If ace is selected, pick the value it has.
def selectAce(card):
    input("You've picked an Ace! Would you like it to be\nof value 1 or 11?")
    if input == '11':
        return 11
    else:
        return 1