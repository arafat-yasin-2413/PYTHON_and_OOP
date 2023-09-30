import pyautogui
# from time import sleep
import time



n = int (input())
time.sleep(5)

for i in range(n):
    for j in range(i+1):
        # print('#',end='')
        pyautogui.write('#')
    # print()
    pyautogui.press('enter')
#
##
###
####
#####








