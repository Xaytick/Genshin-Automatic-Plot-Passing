import pyautogui
import time

import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Code of your program here
    while True:
        pos1 = pyautogui.locateOnScreen('image1.png')
        if pos1:
            print('playing button found')
            pyautogui.click()
        else:
            print('playing button not found')
            pos3 = pyautogui.locateOnScreen('image3.png')
            if pos3:
                pyautogui.click(pos3)
                print('dialog found')
            else:
                print('dialog not found')
               
        time.sleep(0.5)
else:
    # Re-run the program with admin rights
	ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable, __file__, None, 1)


if __name__ == '__main__':
    is_admin()