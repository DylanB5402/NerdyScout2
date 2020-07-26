import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import tbapy
import tbapy.models
import jsbeautifier

import keys

# dict = json.load(open("config_ex.json"))
# print(dict.get("data"))


def gen_config_file_with_tba(input_sheet : str, output_sheet : str, event : str, tba_key : str, google_json : str):
    gen_config_file(input_sheet, output_sheet, get_team_list(event, tba_key), google_json)


def gen_config_file(input_sheet : str, output_sheet : str, team_list : list, google_json : str):
    config_dict = {}
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(google_json, scope)
    client = gspread.authorize(creds)
    input = client.open(input_sheet).sheet1
    input_data = input.get_all_values()
    config_dict.update({"input_headers" : input_data[0]})
    config_dict.update({"teams" : team_list})

    opts = jsbeautifier.default_options()
    opts.indent_size = 2
    with open('config.json', 'w') as fp:
        jsbeautifier.beautify(json.dump(config_dict, fp), opts)


def get_team_list(event : str, tba_key : str) -> list:
    tba = tbapy.TBA(keys.key)
    teams = tba.event_teams(event)
    team_list = []
    for team in teams:
        str_team = team.get('key')
        team_num = int(str_team[3:])
        team_list.append(team_num)
    return sorted(team_list)

# print(get_team_list("2020cala", keys.key))
# NerdyScout2Input
gen_config_file_with_tba("NerdyScout2Input", "NerdyScout2Output", "2020cala", keys.key, "NerdyScoutBlitz-52160ecf0355.json")