import threading
import time
import os

def infiniteloop1():
    while True:
        os.system("python tele.py")
        time.sleep(7200)

def infiniteloop2():
    while True:
        os.system("python tele2.py")
        time.sleep(1)

thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()
