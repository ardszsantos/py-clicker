import keyboard
import time
import threading

stop_flag = False

def press_q():
    while not stop_flag:
        keyboard.press_and_release('q')
        time.sleep(0.5)

def press_s():
    while not stop_flag:
        keyboard.press('s')
        time.sleep(0.1)  

def monitor_stop():
    global stop_flag
    keyboard.wait('-') 
    stop_flag = True


q_thread = threading.Thread(target=press_q)
s_thread = threading.Thread(target=press_s)
monitor_thread = threading.Thread(target=monitor_stop)

q_thread.start()
s_thread.start()
monitor_thread.start()

q_thread.join()
s_thread.join()
