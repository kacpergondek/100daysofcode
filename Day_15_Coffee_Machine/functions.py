from subprocess import call
from os import system, name
import time
import assets

#Clears the screen
def clear():
    _ = call('clear' if name == 'posix' else 'cls')

def printReport():
    print(f"The coffee machine currently has:\n{assets.resources['water']}ml of water\n{assets.resources['milk']}ml of milk\n{assets.resources['coffee']} grams of coffee")

def checkBalance(selection):
    coffee = selection
    if coffee == "cappuccino" or coffee == "c":
        requiredBalance = assets.MENU['cappuccino']['cost']
    elif coffee == "latte" or coffee == "l":
        requiredBalance = assets.MENU['latte']['cost']
    elif coffee == "espresso" or coffee == "e":
        requiredBalance = assets.MENU['espresso']['cost']
    quarterInput = input("How many quarters would you like to insert? ")
    dimeInput = input("How many dimes would you like to insert? ")
    nickleInput = input("How many nickles would you like to insert? ")
    pennyInput = input("How many pennies would you like to insert? ")
    total = (float(quarterInput) * 0.25) + (float(dimeInput) * 0.10) + (float(nickleInput) * 0.05) + (float(pennyInput) * 0.01)
    if total < requiredBalance:
        print(f"You've entered {total}$, but to you need to pay {requiredBalance}$")
        return False
    else:
        change = total - requiredBalance
        return (True, change)

def checkAvailableResources(selection):
    coffee = selection
    availableWater = assets.resources['water']
    availableMilk = assets.resources['milk']
    availableCoffee = assets.resources['coffee']
    if coffee == "cappuccino" or coffee == "c":
        requiredWater = assets.MENU["cappuccino"]["ingredients"]["water"]
        requiredMilk = assets.MENU["cappuccino"]["ingredients"]["milk"]
        requiredCoffee = assets.MENU["cappuccino"]["ingredients"]["coffee"]
    elif coffee == "latte" or coffee == "l":
        requiredWater = assets.MENU["latte"]["ingredients"]["water"]
        requiredMilk = assets.MENU["latte"]["ingredients"]["milk"]
        requiredCoffee = assets.MENU["latte"]["ingredients"]["coffee"]
    elif coffee == "espresso" or coffee == "e":
        requiredWater = assets.MENU["espresso"]["ingredients"]["water"]
        requiredMilk = 0
        requiredCoffee = assets.MENU["espresso"]["ingredients"]["coffee"]
    
    if availableWater < requiredWater:
        print("There is not enough water to complete your order")
        return False 
    elif availableMilk < requiredMilk:
        print("There is not enough milk to complete your order")
        return False
    elif availableCoffee < requiredCoffee:
        print("There is not enough coffee to complete your order")
        return False
    else:
        return True

def makeEspresso(change):
    assets.resources['water'] -= assets.MENU["espresso"]["ingredients"]["water"]
    assets.resources['coffee'] -= assets.MENU["espresso"]["ingredients"]["coffee"]
    print(f"Here is your espresso. Enjoy! Your change: {change} has been refunded")

def makeLatte(change):
    assets.resources['water'] -= assets.MENU["latte"]["ingredients"]["water"]
    assets.resources['milk'] -= assets.MENU["latte"]["ingredients"]["milk"]
    assets.resources['coffee'] -= assets.MENU["latte"]["ingredients"]["coffee"]
    print(f"Here is your latte. Enjoy! Your change: {change} has been refunded")

def makeCappuccino(change):
    assets.resources['water'] -= assets.MENU["cappuccino"]["ingredients"]["water"]
    assets.resources['milk'] -= assets.MENU["cappuccino"]["ingredients"]["milk"]
    assets.resources['coffee'] -= assets.MENU["cappuccino"]["ingredients"]["coffee"]
    print(f"Here is your cappuccino. Enjoy! Your change: {change} has been refunded")
    
def main():
    while True:
        entry = input("What would you like?")
        entry = entry.lower()
        if entry == "help" or entry == "h":
            print("Help")
            clear()
        elif entry == "off" or entry == "quit":
            break
        elif entry == "report" or entry == "r":
            clear()
            printReport()
            time.sleep(3)
            clear()
        elif entry == "cappuccino" or entry == "c":
            x, change = checkBalance('cappuccino')
            if x == True: 
                y = checkAvailableResources('cappuccino')
                if y == True:
                    makeCappuccino(change)
                    time.sleep(2)
                else:
                    continue
            else:
                continue
            clear()
        elif entry == "latte" or entry == "l":
            x, change = checkBalance('latte')
            if x == True: 
                y = checkAvailableResources('latte')
                if y == True:
                    makeLatte(change)
                    time.sleep(2)
                else:
                    continue
            else:
                continue
            clear()
        elif entry == "espresso" or entry == "e":
            x, change = checkBalance('espresso')
            if x == True: 
                y = checkAvailableResources('espresso')
                if y == True:
                    makeEspresso(change)
                    time.sleep(2)
                else:
                    continue
            else:
                continue
            clear()
        else:
            print("Invalid input. Please try again")
    