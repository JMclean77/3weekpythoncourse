import pyautogui
import time
import keyboard

print("You have 5 seconds to hover over the big cookie...")
time.sleep(5)

print("Auto clicker started! Press 'q' to quit.")

try:
    while not keyboard.is_pressed('q'):
        pyautogui.click()
        time.sleep(0.0001)
except KeyboardInterrupt:
    print("Stopped.")
