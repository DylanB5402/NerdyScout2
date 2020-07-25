import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import tbapy
import tbapy.models

import keys

# dict = json.load(open("config.json"))
# print(dict.get("data"))


def gen_config_file_with_tba(input_sheet : str, output_sheet : str, event : str, tba_key : str):
    gen_config_file(input_sheet, output_sheet, get_team_list(event, tba_key))


def gen_config_file(input_sheet : str, output_sheet : str, team_list : list):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("NerdyScoutBlitz-52160ecf0355.json", scope)
    client = gspread.authorize(creds)


def get_team_list(event : str, tba_key : str) -> list:
    tba = tbapy.TBA(keys.key)
    teams = tba.event_teams(event)
    team_list = []
    for team in teams:
        str_team = team.get('key')
        team_num = int(str_team[3:])
        team_list.append(team_num)
    return sorted(team_list)

print(get_team_list("2020cala", keys.key))

