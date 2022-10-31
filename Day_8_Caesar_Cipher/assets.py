# For clear function
from subprocess import call
from os import system, name

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


title = '''
_________                                             _________  .__         .__                     
\_   ___ \ _____     ____    ___________  _______     \_   ___ \ |__|______  |  |__    ____ _______  
/    \  \/ \__  \  _/ __ \  /  ___/\__  \ \_  __ \    /    \  \/ |  |\____ \ |  |  \ _/ __ \\_  __ \ 
\     \____ / __ \_\  ___/  \___ \  / __ \_|  | \/    \     \____|  ||  |_> >|   Y  \\  ___/ |  | \/ 
 \______  /(____  / \___  >/____  >(____  /|__|        \______  /|__||   __/ |___|  / \___  >|__|    
        \/      \/      \/      \/      \/                    \/     |__|         \/      \/         
                                                                                                     
'''

# x is the final message. isalpha detects if what you entered is a letter or not. We modulo the shift to get a remainder, which we then utilize to
# shift the numbers.  

def caesar(direction,text,shift):
    if direction == 'encode':
        x = ""
        for char in text:
            if char.isalpha() == True:
                shift = shift % 26
                char = alphabet.index(char) + shift
                x += alphabet[char]
            else:
                x += char
        print(f"The encoded message is {x}")
    elif direction == 'decode':
        x = ""
        for char in text:
            if char.isalpha() == True:
                shift = shift % 26
                char = alphabet.index(char) - shift
                x += alphabet[char]
            else:
                x += char
        print(f"The decoded message is {x}")

# Main function takes the inputs for the caesar function and then is used to loop the program until the user decides to quit.

def mainfunction():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction,text,shift)
        choice = input("Would you like to continue? \nEnter 'yes' to continue, or 'quit' to quit.\n").lower()
        if choice == 'yes':
            clear()
            continue
        else:
            print("See you!")
            break

def clear():
    _ = call('clear' if name == 'posix' else 'cls')