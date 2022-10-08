import imp
from itertools import count
import pyautogui
import time
time.sleep(4)
count=0
while count<=950:
    pyautogui.typewrite('Hello Someone !!' + str(count))
    pyautogui.press('enter')
    count=count+1