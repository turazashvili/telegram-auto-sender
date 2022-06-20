from time import sleep
import pyautogui
import threading
import keyboard
import pyautogui as p
import threading


names = ["",""] # put names here
itr = iter(names)
itr

sleep(5)

def start():
    while True:
        try:
            sleep(1)
            cords = pyautogui.locateCenterOnScreen('search.png', confidence=0.9)
            pyautogui.moveTo(cords)
            pyautogui.click(cords)
            sleep(1)
            pyautogui.typewrite(next(itr))
            sleep(1)
            pyautogui.click(250,155)
            sleep(1)
            pyautogui.typewrite("what you investing to also?")
            sleep(1)
            p.press('enter')

        except: 
            print("Try again")
        
        # Stops the script with long press of 'S' button on your keyboard.
        if keyboard.is_pressed('s'):
            print("\nYou finished!")
            break
        
threading.Thread(target=start, daemon=True).start()
input('Press Enter to exit.')
