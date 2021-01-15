import gspread
import google_auth_httplib2
import logging
import NameCommandsList
from threading import Thread
from oauth2client.service_account import ServiceAccountCredentials


logging.basicConfig(
    filename='whtLog.log',
    level=logging.DEBUG,
    # format='%(level)s %(asctime)s - %(message)s', datefmt='%H:%M:%S'
)

REGISTER_COMMANDS = NameCommandsList.get_list_register_commands()
QUANTITY_COMMANDS = len(REGISTER_COMMANDS)

def who_end(numberTyr: int, numberAnswer: int, registerCommands=REGISTER_COMMANDS ) -> dict:
    commandsTyr = NameCommandsList.get_list_commands_inTYR(numberTyr)

    whoEnds={}
    
    for comand in REGISTER_COMMANDS:
        for comandTyr in commandsTyr:
            if comand == comandTyr:
                whoEnds[comand] = 'OK'
                break
            whoEnds[comand] = 'NO'
    print(whoEnds)
    return whoEnds        

# a = who_end(1, REGISTER_COMMANDS)



