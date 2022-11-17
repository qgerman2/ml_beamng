import time
import keyboard
from datetime import datetime

def millis():
    return time.time_ns() / 1000000

oldtime = millis()
curtime = 0
rectime = 0
step = 1/60 * 1000 #60 hz

record = False
file = False

while True:
    #manejar teclas
    if (keyboard.is_pressed('a')):
        if (not file):
            filename = datetime.now().strftime("%m %d %Y - %H %M %S") + ".txt"
            file = open(filename, "w")
            rectime = millis()
            print("Grabando: " + filename)
        record = True
    elif (keyboard.is_pressed('s')):
        record = False
        if file:
            file.close()
            file = False
            print("Grabado")
    elif (keyboard.is_pressed('d')):
        record = False
        if file:
            file.close()
            file = False
            print("Grabado")
        print("Fuera del loop")
        break
    #leer sensores
    curtime = millis()
    if curtime > (oldtime + step):
        oldtime = curtime
        if file:
            secs = (curtime - rectime) / 1000
            file.write(str(secs) + '\n')
        