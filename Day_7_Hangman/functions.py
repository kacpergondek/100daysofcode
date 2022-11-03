# Clearing the screen is different on windows and unix-likes.
# Thus, performing a check to get the right ones for right OS.
from subprocess import call
from os import system, name
import graphics
def clear():
    _ = call('clear' if name == 'posix' else 'cls')

def display_graphics(life):
    if life == 6:
        print(graphics.six_lifes)
    elif life == 5:
        print(graphics.five_lifes)
    elif life == 4:
        print(graphics.four_lifes)
    elif life == 3:
        print(graphics.three_lifes)
    elif life == 2:
        print(graphics.two_lifes)
    elif life == 1:
        print(graphics.one_life)
    else:
        print(graphics.zero_lives)