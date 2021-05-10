
import pyautogui, time
time.sleep(4)
# Wait 4 seconds, in this time, you need to click the input that you want to be spammed.
file = open('SPAMTEXT.txt', 'r')


for word in file:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(0.01)