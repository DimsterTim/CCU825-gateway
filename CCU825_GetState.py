# Program to send a command to CCU825


import requests
from CCU_credentials import *

CCU_Command = {'GetStateAndEvents': 'https://ccu.sh/data.cgx?cmd={"Command":"GetStateAndEvents"}',
               'GetDeviceInfo': 'https://ccu.sh/data.cgx?cmd={"Command":"GetDeviceInfo"}'
               }
headers = {'Content-type': 'application/json'}


def CCU_SendCommand(command, login, pswd):

    response = requests.get(command, auth=(login, pswd))
    print(response.url)
    if response.status_code == 200:
        return response.json()
    else:
        print('Ошибка запроса: ' + str(response.status_code))


CCU_JSON = CCU_SendCommand(CCU_Command['GetStateAndEvents'], CCU_Login, CCU_Pass)
print(CCU_JSON)
CCU_JSON = CCU_SendCommand(CCU_Command['GetDeviceInfo'], CCU_Login, CCU_Pass)
print(CCU_JSON)