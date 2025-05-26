import pyautogui

while True:
    if pyautogui.pixel(274, 312) == (75, 219, 106):
        pyautogui.click()
        break
