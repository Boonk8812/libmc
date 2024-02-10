import pyautogui
import time

"""
Test script to make sure Minecraft is working.
"""

# Wait for Minecraft to be in focus
time.sleep(2) # adjust this delay as necessary

# Bring up the chat window by pressing T
pyautogui.hotkey('t')

# Type the chat message and press enter
pyautogui.write("Test", interval=0.1)
pyautogui.press('enter')
