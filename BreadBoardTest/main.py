from machine import Pin
from network import LoRa
import time
import ubinascii
import pycom

led = Pin('G23', mode = Pin.OUT)

lora = LoRa(mode=LoRa.LORAWAN)

app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('A73D67D5609F6CA1D4B44C0304961A09')
dev_eui = ubinascii.unhexlify('70B3D5499885FADE')

lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')
print('Joined')
led.value(1)