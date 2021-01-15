import gspread
import google_auth_httplib2
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'] # что то для чего-то нужно Костыль    
CREDS = ServiceAccountCredentials.from_json_keyfile_name("/Users/igorgerasimov/Desktop/Мусор/CAEPKGTA-72e4d28af1d1.json", SCOPE) # Секретынй файл json для доступа к API
CLIENT = gspread.authorize(CREDS)

# alfavit = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']


def get_list_register_commands() -> list:
    SHEET_REGISTER = CLIENT.open('1_TYR').worksheet('Register')
    nameCommand = SHEET_REGISTER.get(f'B1')
    _index = 1
    NAME_COMMANDS = []
    
    while nameCommand[0][0] is not None:
        try:
            _index += 1
            NAME_COMMANDS.append(SHEET_REGISTER.get(f'B{_index}')[0][0])
        except:
            return NAME_COMMANDS


def get_list_commands_inTYR(numberTYR: int) -> list:
    SHEET_TYR = CLIENT.open('1_TYR').worksheet(f'{numberTYR}TYR')
    nameCommand = SHEET_TYR.get(f'B1')
    _index = 1
    NAME_COMMANDS_inTYR = []

    while nameCommand[0][0] is not None:
        try:
            _index += 1
            NAME_COMMANDS_inTYR.append(SHEET_TYR.get(f'B{_index}')[0][0])
        except:
            return NAME_COMMANDS_inTYR


def get_list_answer_inTyr(numberTYR: int, numberAnswer: int) -> list:
    SHEET_TYR = CLIENT.open('1_TYR').worksheet(f'{numberTYR}TYR')
    nameCommand = SHEET_REGISTER.get(f'B1')
    _index = 1
    NAME_COMMANDS_inTYR = []

    while nameCommand[0][0] is not None:
        try:
            _index += 1
            NAME_COMMANDS_inTYR.append(SHEET_TYR.get(f'B{_index}')[0][0])
        except:
            return NAME_COMMANDS_inTYR

# def get_dict_answer_commands(comandTyr: list, answers: list) -> dict:
#     answerComands = {}

#     for 



