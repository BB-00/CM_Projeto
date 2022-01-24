import pycom
import time

pycom.heartbeat(False)

while True:
    # colors in hexadecimal (0xRRGGBB)
    pycom.rgbled(0xFF0000) # red
    time.sleep(1)
    pycom.rgbled(0x00FF00) # green
    time.sleep(1)
    pycom.rgbled(0x0000FF) # blue
    time.sleep(1)
    pycom.rgbled(0xFFFFFF) # white
    time.sleep(1)
    pycom.rgbled(0xFB48C4) # pink
    time.sleep(1)