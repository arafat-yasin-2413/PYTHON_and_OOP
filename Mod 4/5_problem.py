import pyautogui
# from time import sleep
import time

time.sleep(2)

n = int (input())
for i in range(n):
    for j in range(i+1):
        # print('#',end='')
        pyautogui.write('#')
    # print()
    pyautogui.press('enter')








