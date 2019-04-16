# Program to send a command to CCU825
import json


import requests
from CCU_credentials import *


CCU_Parameters = {"Command":"GetStateAndEvents"}
CCU_Command = CCU_Parameters
headers = {'Content-type': 'application/json'}


print(CCU_Command)


def CCU_SendCommand(login, pswd): #, headers):

    response = requests.get('https://ccu.sh/data.cgx', json={'cmd': CCU_Command}, auth=(login, pswd)) #, headers=headers)
    print(response.url)
    if response.status_code == 200:
        return response.json()
    else:
        print('Ошибка запроса: ' + str(response.status_code))


CCU_JSON = CCU_SendCommand(CCU_Login,CCU_Pass) #, headers)
print(CCU_JSON)
