import pyautogui
import pyperclip
import time

# Small delay before starting (so you can switch to the right window)
time.sleep(1)

# Step 1: Click on the icon at (1290, 1050)
pyautogui.click(1290, 1050)
time.sleep(1)

# Step 2: Drag from (448, 228) to (935, 970) to select text
pyautogui.moveTo(497, 247)
pyautogui.dragTo(919, 966, duration=1, button='left')
# time.sleep(1)

# Step 3: Copy (Ctrl + C)
pyautogui.hotkey("ctrl", "c")
pyautogui.click(850, 850)
time.sleep(1)

# Step 4: Paste from clipboard into a Python variable
copied_text = pyperclip.paste()

# print("Copied Text:")
print(copied_text)
