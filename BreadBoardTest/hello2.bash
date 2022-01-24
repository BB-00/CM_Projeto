curl --location \
  --header 'Authorization: Bearer NNSXS.OQZK3C2H4ATSAS3XSGH6P53FR57HXOR2Q6CJ2IQ.EHOYARJUSS3J5TJWIMFG5KXCBNBHIV5WPMUWGP65Q5VYGI3WZXXA' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: my-integration/my-integration-version' \
  --request POST \
  --data '{"downlinks":[{
      "decoded_payload": {
        "bytes": [1, 2, 3]
      }
    }]
  }' \
  'https://thethings.example.com/api/v3/as/applications/cm-projeto/webhooks/basket/devices/eui-70b3d5499885fade/down/push'