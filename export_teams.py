import csv
import requests
import json
import pandas as pd
import sys

api_key = '<your api key>'
team_data_csv = './teamList.csv' # set this to your desired path or leave the same to generate csv in same directory
api_headers = {'Content-Type': 'application/json','Authorization':'GenieKey ' + api_key}
list_team_url = "https://api.opsgenie.com/v2/teams/" 
expand_params = {'expand': 'contact'}


def build_team_list(api_key, url, api_headers):
    team_list_request = requests.get(url = list_team_url, headers = api_headers)
    team_json = json.loads(team_list_request.text) 
    teams = []
    
    for team in team_json['data']:
    	teams.append(team['name'])

    return teams

def generate_csv(teams):
    df = pd.DataFrame(teams)
    df.to_csv(team_data_csv, sep=',', encoding='utf-8')

teams = build_team_list(api_key, list_team_url, api_headers)
generate_csv(teams)