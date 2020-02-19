import pyautogui, sys
import time as time
from random import randint
pyautogui.FAILSAFE = True
print('Press Ctrl-C to quit.')
try:
    while True:
        a = randint(2, 10)
        print(a)
        time.sleep(a)
        pyautogui.keyDown('w')
        pyautogui.keyUp('w')
except KeyboardInterrupt:
    print('\n')
