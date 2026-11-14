#Football game automater

import pydirectinput
import time
import keyboard
import os

#Important coords and timer

play_button = (972, 969)
play_again_button = (1183, 917)

#Break

keyboard.add_hotkey('q', lambda: os._exit(0))

#Function

def start_game():
    pydirectinput.moveTo(*play_button)
    pydirectinput.moveRel(1, 0)
    pydirectinput.leftClick()

def game_loop():
    pydirectinput.moveTo(*play_again_button)
    pydirectinput.moveRel(1, 0)
    pydirectinput.leftClick()
    time.sleep(5)

main_loop = True
counter = 0

while main_loop is True:

    if counter == 0:
        time.sleep(3)
        start_game()
        counter =  counter + 1

    elif counter > 0:
        game_loop()