import imp
from itertools import count
import pyautogui
import time
time.sleep(5)
count=0
while count<=950:
    pyautogui.typewrite('```python -m pip install --upgrade pip P.S. this solution works for other modules too.Ive   \
        installed Django and few other packages before but somehow the pyautogui just cant seemed to go```' + str(count))
    pyautogui.press('enter')
    count=count+1
