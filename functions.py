import random
import time
import game_data
import assets
from subprocess import call
from os import system, name

#Clears the screen
def clear():
    #from subprocess import call
    # #from os import system, name
    _ = call('clear' if name == 'posix' else 'cls')

#The function will take the length of the list and then this information will be used to randomly select the items in the dataset
def datasetLen(dataset):
    datalength = len(dataset) - 1
    return datalength

#The function picks a random item from the game data
def pickRandom():
    max_value = datasetLen(game_data.data)
    randnum = random.randint(0,max_value)
    return(game_data.data[randnum])

#The function extracts the dictionary data and prints information about the person
def dataExtract(person):
    vowel_list = ['a','e','i','o','u']

    if (person['description'][0].lower() in vowel_list):
        a_or_an = ("an")
    else:
        a_or_an = ("a")

    print(f"{person['name']},\n{a_or_an} {person['description']}  \nfrom {person['country']}")
    return person

def main():
    score = 0
    defeat = False
    person1 = pickRandom()
    person2 = pickRandom()

    while defeat == False:
        #Prevent same two people being present
        if person1 == person2:
            person2 = pickRandom()
        # Count the number of followers on each person.
        count1 = int(person1['follower_count'])
        count2 = int(person2['follower_count'])
        print (assets.mainart)
        print(f"Your current score is {score}")
        dataExtract(person1)
        print("\nvs\n")
        dataExtract(person2)
        answer = input("Which person has more followers? Person 1 or Person 2?")
        if answer == "1":
            if count1 > count2:
                score += 1
                person1 = person2
                person2 = pickRandom()
                clear()
            else:
                defeat == True
                print(f"You lost with {score} points")
                break
        elif answer == "2":
            if count2 > count1:
                score += 1
                person1 = person2                
                person2 = pickRandom()
                clear()
            else:
                print(f"You lost with {score} points")
                break     
