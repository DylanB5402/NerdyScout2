import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# dict = json.load(open("config.json"))
# print(dict.get("data"))


def gen_config_file(input_url : str, output_url : str, event : str):
    pass


def gen_config_file(input_url : str, output_url : str, team_list : list):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("NerdyScoutBlitz-52160ecf0355.json", scope)
    client = gspread.authorize(creds)


def get_team_list(event : str):
    pass

