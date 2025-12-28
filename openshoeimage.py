import pyautogui
import time

time.sleep(3)
pyautogui.hotkey('win', 'e')

time.sleep(2)
pyautogui.click(1040, 752)
time.sleep(1)
pyautogui.doubleClick(1040, 752)

time.sleep(2)

for i in range(8):
    pyautogui.hotkey('tab')
    time.sleep(0.3)

time.sleep(3)
pyautogui.write('Pictures\Screenshots')
time.sleep(2)
pyautogui.press('enter')

pyautogui.hotkey('ctrl', 'f')
time.sleep(0.5)
pyautogui.scroll(400)
pyautogui.typewrite("nikesmartshoe")

time.sleep(0.5)
location = pyautogui.locateOnScreen("nikescreen.png", confidence = 0.8)
print("location")

pyautogui.tripleClick(pyautogui.center(location))


