import time
import os

start = time.time()
seconds = 0
minutes = 0

while True:
    seconds = int(time.time() - start) - minutes * 60
    clear = lambda: os.system('cls')
    clear = lambda: os.system('clear')
    clear()
    print ("\r{minutes} Perc {seconds} Másodperc".format(minutes=minutes, seconds=seconds))
    if seconds >= 60:
        minutes += 1
        seconds = 0