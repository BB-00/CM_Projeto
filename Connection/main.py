#from network import LoRa
#import time
#import binascii

# Initialise LoRa in LORAWAN mode .
#lora = LoRa(mode=LoRa.LORAWAN)
# create an OTAA authentication parameters , change them to the provided credentials
#app_eui = ubinascii.unhexlify('0000000000000000')
#app_key = ubinascii.unhexlify('9AD6D8AA38F15B8081342C066C4D9068')
#dev_eui = ubinascii.unhexlify('70B3D5499885FADE')
# join a network using OTAA ( Over the Air Activation )
#lora.join(activation=LoRa.OTAA, auth =(dev_eui, app_eui ,app_key ), timeout=0)
# wait until the module has joined the network
#while not lora.has_joined():
#    print('Not yet joined ... ')
#    time.sleep(2.5)

#print ('Joined ')

# ----------------------------------------------------------
# ----------------------------------------------------------

#from network import LoRa
#import binascii
#print(binascii.hexlify(LoRa().mac()).upper())

# ----------------------------------------------------------
# ----------------------------------------------------------

from network import LoRa
import socket
import time
import ubinascii
import pycom

# Initialise LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an OTAA authentication parameters, change them to the provided credentials
app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('6A39CF4AC142C7AD55A1C01556D69483')
#uncomment to use LoRaWAN application provided dev_eui
dev_eui = ubinascii.unhexlify('70B3D5499885FADE')

# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')
pycom.heartbeat(False)
pycom.rgbled(0xFFFFFF) # white
print('Joined')
# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# send some data
s.send(bytes([0x01, 0x02, 0x03]))

# make the socket non-blocking
# (because if there's no data received it will block forever...)
s.setblocking(False)

# get any data received (if any...)
data = s.recv(64)
print(data)