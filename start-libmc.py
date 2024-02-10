import pyautogui
import time

# Wait for Minecraft to be in focus
time.sleep(2) # adjust this delay as necessary

# Bring up the chat window by pressing T
pyautogui.hotkey('t')

# Type the chat message and press enter
pyautogui.write("Starting libmc...", interval=0.1)
pyautogui.press('enter')
