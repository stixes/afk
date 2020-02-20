import pyautogui, sys
import time as time
from random import randint,choice
pyautogui.FAILSAFE = True
print('Press Ctrl-C to quit.')
try:
    while True:
        a = randint(100, 300)
        c = randint(1,10)
        print(a)
        time.sleep(a)
        for i in range(1,c):
            k = choice(['a','s','w','d','b','x',' '])
            pyautogui.keyDown(k)
            time.sleep(0.05)
            pyautogui.keyUp(k)
except KeyboardInterrupt:
    print('\n')
