import pyautogui
import time
import pyperclip

print(pyautogui.position())
time.sleep(1)
pyautogui.moveTo(-3000, 800, 0)
pyautogui.click(button='left')
pyperclip.copy("안녕 잘가 ")
pyautogui.hotkey('ctrl', 'v')