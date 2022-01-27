from machine import Pin
from network import LoRa
import time
import ubinascii
import socket

led = Pin('G23', mode = Pin.OUT)

lora = LoRa(mode=LoRa.LORAWAN)

app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('D078A5255AFBF12FBE203CB11C27DAA9')
dev_eui = ubinascii.unhexlify('70B3D5499885FADE')

lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')
print('Joined')

# create LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(False)

#OLD CHECK_DOWNLINL()
#def check_downlink():
#    data = s.recv(64)
#    print("Downlink Check", i)
#    if not data :
#        return
#    print ("Receive: Value: ", data)
#    return data

def check_downlink():
    print("Downlink Check", i)

    s.settimeout(2.0) # configure a timeout value of 3 seconds

    try:
        rx_pkt = s.recv(64) # get the packet received (if any)
        print(rx_pkt)
        return rx_pkt
    except socket.timeout:
        print('No packet received')
        return

gpio = Pin('G23', mode = Pin.OUT)
ledOn=False
while True:
    if (lora.has_joined()):
        # UPLINK
        if (gpio.value()==1):
            s.send(bytes([0x01]))
            print("Send: Value: ", gpio.value(), " -> on")
        elif(gpio.value()==0):
            s.send(bytes([0x00]))
            print("Send: Value: ", gpio.value(), " -> off")

        # DOWNLINK
        data=0
        for i in range (5):
            data = check_downlink()
            if (data != None):
                break

        if(data== b'\x01'):
            ledOn = True
        elif(data == b'\x00'):
            ledOn = False

        time.sleep(1)

        if(ledOn):
            gpio.value(1)
        else:
            gpio.value(0)
