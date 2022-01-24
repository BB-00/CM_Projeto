import requests
import time


URL = "https://eu1.cloud.thethings.network/console/applications/cm-projeto/webhooks/basket/devices/eui-70b3d5499885fade/down/push"
#URL = "https://eu1.cloud.thethings.network/console/applications/cm-projeto/devices/eui-70b3d5499885fade/messaging/downlink"

requests.post(URL,headers = {'Authorization':'NNSXS.OQZK3C2H4ATSAS3XSGH6P53FR57HXOR2Q6CJ2IQ.EHOYARJUSS3J5TJWIMFG5KXCBNBHIV5WPMUWGP65Q5VYGI3WZXXA', 'Content-Type':'application/json','User-Agent':'my-integration/my-integration-version'}, data = {"downlinks":[{"decoded_payload": {"bytes": [1,2,3]}}]})

requests.post(URL, headers={''})