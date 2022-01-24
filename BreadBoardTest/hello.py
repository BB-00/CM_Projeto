from network import LoRa
import time
import ubinascii
import socket

lora = LoRa(mode=LoRa.LORAWAN)

app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('EEFF7C9A6A48D2D5137CB7D662FFBB7E')
dev_eui = ubinascii.unhexlify('70B3D5499885FADE')

lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')
print('Joined')

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(False)
while True:
    s.send(bytes([1, 2, 3]))
    s.settimeout(3.0) # configure a timeout value of 3 seconds

    try:
        rx_pkt = s.recv(64)   # get the packet received (if any)
        print(rx_pkt)
    except socket.timeout:
        print('No packet received')