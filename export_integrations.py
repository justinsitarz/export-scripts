import csv
import requests
import json
import pandas as pd
import sys

api_key = '<your api key>'
integration_data_csv = './integrationList.csv' # set this to your desired path or leave the same to generate csv in same directory
api_headers = {'Content-Type': 'application/json','Authorization':'GenieKey ' + api_key}
list_integration_url = "https://api.opsgenie.com/v2/integrations/" 
expand_params = {'expand': 'contact'}


def build_integration_list(api_key, url, api_headers):
    integration_list_request = requests.get(url = list_integration_url, headers = api_headers)
    integration_json = json.loads(integration_list_request.text) 
    integrations = []
    
    for integration in integration_json['data']:
    	integrations.append(integration['name'])

    return integrations

def generate_csv(integrations):
    df = pd.DataFrame(integrations)
    df.to_csv(integration_data_csv, sep=',', encoding='utf-8')

integrations = build_integration_list(api_key, list_integration_url, api_headers)
generate_csv(integrations)