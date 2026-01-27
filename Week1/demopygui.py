import pyautogui
import time


#Mouse operations
pyautogui.click(80,80)
time.sleep(2)
pyautogui.rightClick(80,80)

time.sleep(2)

pyautogui.click(1388,27)
pyautogui.leftClick(1388,27)
pyautogui.doubleClick(80,80)

#pyautogui.drag(80,80, 100,100)
pyautogui.scroll(340)
#My PyAutoGUI Demo
#Successful

#keyboard operations

time.sleep(2)
pyautogui.click(436,274)

time.sleep(2)

pyautogui.typewrite("#My PyAutoGUI Demo")

time.sleep(3)
pyautogui.press("enter")

time.sleep(2)
pyautogui.write("#Successful")

time.sleep(3)
pyautogui.hotkey('ctrl', 'a')


#image operations

print(pyautogui.size())

ss = pyautogui.screenshot()

ss.save("ssdemo.png")