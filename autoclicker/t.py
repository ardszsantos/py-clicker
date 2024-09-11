import pyautogui
import time
import keyboard

print("O script começará em 3 segundos...")
time.sleep(3)

x, y = pyautogui.position()
interval = 0.0001

print("Pressione 'q' para parar o autoclicker.")

try:
    while True:
        if keyboard.is_pressed('q'):
            print("Autoclick interrompido.")
            break
        pyautogui.click(x=x, y=y)
        time.sleep(interval)
except KeyboardInterrupt:
    print("Autoclick interrompido manualmente.")
