import pandas as pd
import turtle

DATA_PATH = '/home/kednog/Pulpit/us-states-game-start/50_states.csv'
IMAGE_PATH = '/home/kednog/Pulpit/us-states-game-start/blank_states_img.gif'

data = pd.read_csv(DATA_PATH)
state_data = data.set_index('state')

def retrieve_coordinates(state):
    data = state_data.loc[state]
    x = data['x']
    y = data['y']
    return x, y

def state_write(name, position):
    entry = turtle.Turtle(visible=False)
   # entry.hideturtle()
    entry.penup()
    entry.setpos(position)
    entry.write(name)
    

sc = turtle.Screen()
sc.bgpic(IMAGE_PATH)


correct_guesses = 0
guessed_states = []
turtle.penup()

#Game main loop
while True:
    
    if correct_guesses == 50:
        break

    entry = sc.textinput(f"You guessed {correct_guesses}/50 states", 'Name a state')
    state_input = entry.title()
    
    # If a new entry is found, append to list and find the coordinates
    if ((state_data.index == state_input).any()) and not (state_input in guessed_states):
        guessed_states.append(state_input)
        correct_guesses += 1
        coordinates = retrieve_coordinates(state_input)
        state_write(state_input, coordinates)
    elif state_input == 'Exit':
        not_guessed_states = []
        for name in state_data.index:
            if name not in guessed_states:
                not_guessed_states.append(name)
        f = open("States to Learn","w")
        for item in not_guessed_states:
            f.write(item + "\n")
        f.close()
        break

    else:
        pass



