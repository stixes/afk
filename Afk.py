import pyautogui, sys
import time as time
from random import randint,choice,gauss
pyautogui.FAILSAFE = True
print('Press Ctrl-C to quit.')
try:
    while True:
        #a = randint(100, 300)
        a = max(gauss(10*60,2*60),0)
        c = randint(2,5)
        print("Seconds to next input %d"%a)
        time.sleep(a)
        print("Waking up..")
        for i in range(1,c):
            k = choice([' '])
            pyautogui.keyDown(k)
            time.sleep(gauss(0.06,0.02))
            pyautogui.keyUp(k)
            time.sleep(gauss(0.5,0.1))
        print("Back to sleep.")
except KeyboardInterrupt:
    print('\n')
