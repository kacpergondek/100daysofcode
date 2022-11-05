from subprocess import call
from os import system, name

maintext = '''
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  
 '''

def clear():
    _ = call('clear' if name == 'posix' else 'cls')


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def main():
    clear()
    print(maintext)
    number1 = float(input("Please enter first number: \n"))
    while True:
        for value in operations:
            print(value)
        operation = input("Please select the operation that you want to perform: \n")
        number2 = float(input("Please enter second number: \n"))
        calculation = operations[operation](number1, number2)
        print(f"{number1} {operation} {number2} = {calculation}")
        x = input(f"Would you like to continue on calculating with answer {calculation}, or start a new one?\n (C)ontinue or (N)ew?\n").lower()
        if x == 'c':
            clear()
            number1 = calculation
        elif x == 'n':
            clear()
            main()
        else:
            break





