import requests
import time


URL = "https://rbaskets.in/api/baskets/mm5ia12/requests" 

requests.post(URL,headers = {'Authorization':'A9Fk5pyVyZX7Q_vs0MJF-AwUe1MLGeEQZRhS1uztuOx6'}, data = {"led" : "on"})

while True :
    
    response = requests.get(URL, headers = {'Authorization':'A9Fk5pyVyZX7Q_vs0MJF-AwUe1MLGeEQZRhS1uztuOx6'}, params={'max':'1'})

    if (response.status_code == 200):
        print("ok")
    elif (response.status_code == 204):
        print("No content")
    elif (response.status_code == 401):
        print("Unauthorized. Invalid or missing token")
    else:
        print("Not found")
    
    response = response.json()

    response_body = response.get("requests")[0]['body']
    print(response_body)
    time.sleep(5)