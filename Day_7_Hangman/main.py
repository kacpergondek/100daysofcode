import language
import graphics
import functions

import random
import time

language_selected = []
word_bank = []
graphics_language = ""
victory = ""
defeat = ""
title = ""

# Lower case language selection, and depending on the input, the game loads the list 
# with languages as language_selected, word bank for each language as word_bank, and
# graphics for languages as a string graphics_language

language_entry = input('''Please select your language/Proszę wybrać język


English (ENG)

Polski (PL)

''')

language_choice = language_entry.lower()
if language_choice == "polski" or language_choice == "pl":
    print ("Wybrałeś/aś język polski")
    word_bank = language.polish_bank
    language_selected = language.text_polish
    graphics_language = "pl"
    print (language_selected[0])

elif language_choice == "english" or language_choice == "eng":
    print ("You've selected English")
    word_bank = language.english_bank
    language_selected = language.text_english
    print (language_selected[0])
    graphics_language = "en"

else:
    print ("I cannot understand your input, therefore\ni will default the game to English")
    word_bank = language.english_bank
    language_selected = language.text_english
    print (language_selected[0])
    graphics_language = "en"

# String graphics_language is utilized to now give variables the names of language specific
# graphics which are to be utilized in the game

if graphics_language == "pl":
    victory = graphics.pl_victory
    defeat = graphics.pl_defeat
    title = graphics.pl_title
elif graphics_language == "en":
    victory = graphics.en_victory
    defeat = graphics.en_defeat
    title = graphics.en_title

game_over = False

# Imitates loading and allows the user to read the messages prior to title screen

time.sleep(1)

# Main game 

functions.clear()
print(title)
time.sleep(2)

# We pick a random word from the bank, we create a list from that word 
# (for victory check)

if game_over == False:
    functions.clear()
    word_chosen = random.choice(word_bank)
    list_word_chosen = list(map(str, word_chosen))
    life = 6
    blank_list = []

    #Get the length of the word and create a blank list to fill

    for i in range(len(word_chosen)):
        blank_list.append('_')

    #While loop containing the game proper

    while blank_list != list_word_chosen:
        functions.clear()

        # If you lose all lifes, break the loop

        if life <= 0:
            print(defeat)
            time.sleep(2)
            game_over == True
            break

        # Display the hangman and the list of letters to be filled
        # Then, ask for input and make it lower case

        # Star in the back of blank_list makes it look better

        functions.display_graphics(life)
        print (*blank_list)
        enter = input(('\n' + language_selected[1] + '\n'))
        x = enter.lower()

        # For each position in word_chosen, if it equals to the input,
        # add it to the blank list on the same position
 
        for position in range(len(word_chosen)):
            letter = word_chosen[position]
            if letter == x:
                blank_list[position] = x

        # Lose life if letter does not exist

        if x not in word_chosen :
             print(language_selected[2])
             time.sleep(1)
             life -= 1

    else:
        functions.clear()
        print(victory)
        time.sleep(2)

#Bugs to be sorted later:
# If user enters two correct letters (e.g. to in cryp__currencies) then nothing happens

