#!/usr/bin/env python3
# Program to send a command to CCU825

import json
import requests
from CCU_credentials import *
from flask_api import FlaskAPI
from flask import request

CCU_Command = {'GetStateAndEvents': {"Command":"GetStateAndEvents"},
               'GetDeviceInfo':     {"Command":"GetDeviceInfo"},
               'SetOutputsState':   {"Command":"SetOutputsState","State":[-1,-1,-1,-1,-1,-1,-1]}
               }


app = FlaskAPI(__name__)


@app.route("/GetStateAndEvents/", methods=['GET', 'POST'])
def GetStateAndEvents():
    try:
        CCU_JSON = CCU_SendCommand(CCU_Command['GetStateAndEvents'], CCU_Login, CCU_Pass)
        print(CCU_JSON)
        return CCU_JSON
    except:
        return {'Invalid': 'request'}

@app.route("/GetDeviceInfo/", methods=['GET', 'POST'])
def GetDeviceInfo():
    try:
        CCU_JSON = CCU_SendCommand(CCU_Command['GetDeviceInfo'], CCU_Login, CCU_Pass)
        print(CCU_JSON)
        return CCU_JSON
    except:
        return {'Invalid': 'request'}


@app.route("/SetOutputsState/", methods=['GET', 'POST'])
def SetOutputsState():
    try:
        getoutputstate = request.data
        if len(getoutputstate.get('State')) == 7:
            CCU_Command["SetOutputsState"]["State"] = getoutputstate.get('State')
            #print("Запрашиваемое состояние: %" % (CCU_Command["SetOutputsState"]["State"]))
            CCU_JSON = CCU_SendCommand(CCU_Command['SetOutputsState'], CCU_Login, CCU_Pass)
            print(CCU_JSON['Outputs'])
            return CCU_JSON
        else:
            return {'Invalid': 'request'}
    except Exception as ex:
        print(ex)
        return {'Shit': 'Happened'}


# Обработчик запросов к CCU.SH
def CCU_SendCommand(command, login, pswd):

    response = requests.get('https://ccu.sh/data.cgx', params='cmd='+json.dumps(command, separators=(',', ':')), auth=(login, pswd))
    if response.status_code == 200:
        return response.json()
    else:
        print('Ошибка подключения: ' + str(response.status_code))


def start(Server_Port):
    app.run(host='0.0.0.0',port=Server_Port)

    return()



# тест подключения к CCU.SH
CCU_JSON = CCU_SendCommand(CCU_Command['GetStateAndEvents'], CCU_Login, CCU_Pass)
if CCU_JSON != None:
    print('Успешное подключение к CCU.SH, запускаю сервер..')
    #for i in CCU_JSON.items():
    #    print('{} - {}'.format(i, ', '.join(i[1])))

    print(CCU_JSON)
    print(CCU_JSON['Outputs'])

    CCU_Command["SetOutputsState"]["State"] = CCU_JSON['Outputs']
    print(CCU_Command["SetOutputsState"]["State"])

    # Запуск сервера
    if __name__ == "__main__":
        start(Server_Port)

else: print('Что-то пошло не так..')




