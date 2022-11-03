from subprocess import call
from os import system, name

def clear():
    _ = call('clear' if name == 'posix' else 'cls')

bids = {}

def mainfunction():
    while True:
        name = input ("Please enter your name:\n")
        bid = input ("Please enter tne bid amount:\n£")
        addToDictionary(name, bid, bids)
        x = input("Is there another bidder? Type 'yes' or 'no'\n").lower()
        if x == 'yes':
            clear()
            continue
        else:
            clear()
            highestBidder(bids)
            break


def addToDictionary(name, bid, dictionary):
    dictionary[name] = bid

def highestBidder(dictionary):
    highestAmount = 0
    name = ""
    for bidder in dictionary:
        x = dictionary[bidder]
        bid = int(x) 
        if bid > highestAmount:
            highestAmount = bid
            name = bidder
    print(f"The auction is won by {name} who bid £{highestAmount}")