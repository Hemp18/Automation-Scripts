#Saber Sim automation bot

import time
import pydirectinput
import keyboard
import os

keyboard.add_hotkey('q', lambda: os._exit(0))
saber_shop_button = (598, 336)
dna_shop_button = (907, 338)
class_shop_button = (1347, 343)
saber_sword_shop_grids=[(589, 464), (707, 457), (832, 462), (937, 456), (1059, 463), (587, 580), (694, 572), (825, 577), (944, 575), (1067, 579), (595, 689), (711, 702), (832, 701), (949, 703), (1069, 694)]
saber_dna_shop_grids =[(589, 464), (707, 457), (832, 462), (937, 456), (1059, 463), (587, 580), (694, 572), (825, 577), (944, 575), (1067, 579), (595, 689), (711, 702), (832, 701), (949, 703), (1069, 694)]
buy_all_button = (1344, 783)
buy_all_confirmation = (826, 650)
buy_all_exit = (1241, 349)
sell_button = (1852, 348)
sell_exit_button = (1244, 331)
exit_button = (1392, 256)
center = (535, 216)

def swing_and_sell():
    for swing in range(150):
        pydirectinput.click()
        time.sleep(0.5)
    pydirectinput.moveTo(*sell_button)
    time.sleep(0.3)
    pydirectinput.moveRel(1, 0)   # tiny nudge so the game registers a hover
    time.sleep(0.1)
    pydirectinput.mouseDown()
    time.sleep(0.1)
    pydirectinput.mouseUp()
    time.sleep(0.5)
    pydirectinput.moveTo(*center)
    time.sleep(0.3)
    for _ in range(2):
        pydirectinput.moveRel(10, 0)
        time.sleep(0.1)
        pydirectinput.moveRel(-10, 0)
        time.sleep(0.1)
    pydirectinput.click()
    time.sleep(0.8)
    pydirectinput.keyDown('w')
    try:
        time.sleep(1)
    finally:
        pydirectinput.keyUp('w')

def saber_shop():
    pydirectinput.keyDown('w')
    try:
        time.sleep(4)
    finally:
        pydirectinput.keyUp('w')
    pydirectinput.leftClick(*saber_shop_button)
    pydirectinput.moveRel(1, 0)
    pydirectinput.leftClick()
    pydirectinput.leftClick(*buy_all_button)
    pydirectinput.moveRel(1, 0)
    pydirectinput.leftClick()
    time.sleep(0.5)
    pydirectinput.leftClick(*exit_button)
    pydirectinput.moveRel(1, 0)
    pydirectinput.leftClick()
    time.sleep(0.5)
    pydirectinput.moveRel(1, 0)
    pydirectinput.keyDown('s')
    try:
        time.sleep(2)
    finally:
        pydirectinput.keyUp('s')

def dna_shop():
    pydirectinput.keyDown('w')
    try:
        time.sleep(4)
    finally:
        pydirectinput.keyUp('w')
    pydirectinput.leftClick(*dna_shop_button)
    pydirectinput.moveRel(1, 0)
    pydirectinput.leftClick()
    time.sleep(0.5)
    pydirectinput.leftClick(*buy_all_button)
    pydirectinput.moveRel(1, 0)
    pydirectinput.leftClick()
    time.sleep(0.5)
    pydirectinput.leftClick(*buy_all_confirmation)
    pydirectinput.moveRel(1, 0)
    pydirectinput.leftClick()
    time.sleep(1)
    pydirectinput.leftClick(*exit_button)
    pydirectinput.moveRel(1, 0)
    pydirectinput.leftClick()
    time.sleep(0.5)
    pydirectinput.moveRel(1, 0)
    pydirectinput.keyDown('s')
    try:
        time.sleep(2)
    finally:
        pydirectinput.keyUp('s')


main_loop = True
counter = 0
dna_countdown = 0

time.sleep(5)
while main_loop is True:
    if keyboard.is_pressed('q'):
        break
    elif counter < 3:
        swing_and_sell()
        counter = counter + 1
        dna_countdown = dna_countdown + 1
    
    elif dna_countdown == 9:
        dna_shop()
        dna_countdown = 0
    
    else:
        saber_shop()
        counter = 0

    try:
        success_count += 1
    except NameError:
        success_count = 1

    if success_count >= 2:
        print("\a")
        import sys; sys.stdout.flush()
        break