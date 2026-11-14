#C.D.G


import pydirectinput
import time
import keyboard
import os
import winsound

#Killswitch
keyboard.add_hotkey('q', lambda: os._exit(0))

#Important coords command
#python -c "import pyautogui; pyautogui.displayMousePosition()"

#Important coords
cases_shop_button = (978, 958)
howl_case = (1132, 498)
auto_role_on = (727, 177)
auto_role_off = (727, 177)
buy_button = (1020, 433)

inventory = (833, 944)
select_all = (987, 282)
sell_selected = (1288, 736)

screen_center = (889, 505)

def case_n_buy():
    pydirectinput.moveTo(*cases_shop_button)
    pydirectinput.moveRel(1, 0)
    pydirectinput.leftClick(*cases_shop_button)
    time.sleep(0.5)
    pydirectinput.moveTo(*howl_case)
    pydirectinput.moveRel(1, 0)
    pydirectinput.leftClick(*howl_case)
    time.sleep(0.5)
    pydirectinput.moveTo(*buy_button)
    pydirectinput.moveRel(1, 0)
    pydirectinput.leftClick(*buy_button)
    time.sleep(2)
    

def roll():
    for i in range(50):
         pydirectinput.keyDown('r')
         time.sleep(0.8)
         pydirectinput.keyUp('r')
         time.sleep(1.5)


def inventory_n_sell():
     pydirectinput.moveTo(*inventory)
     pydirectinput.moveRel(1, 0)
     pydirectinput.leftClick(*inventory)
     time.sleep(0.5)
     for _ in range(5):
        pydirectinput.moveTo(*select_all)
        pydirectinput.moveRel(1, 0)
        pydirectinput.leftClick(*select_all)
        time.sleep(0.5)
        pydirectinput.moveTo(*sell_selected)
        pydirectinput.moveRel(1, 0)
        pydirectinput.leftClick(*sell_selected)
     
main_loop = True
opening = True
spins = 0

time.sleep(2)

while main_loop is True:
    
    
    if opening is True:
        case_n_buy()
        opening = False

    else:
         for i in range(3):
            roll()
            spins = spins + 1

    if spins == 3:
        print("Final stage reached")
        winsound.PlaySound("ping sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        inventory_n_sell()
        time.sleep(1)
        opening = True
        spins = 0
        print("Final stage executed, resetting loop...")