import csv
import requests
import json
import pandas as pd
import sys

api_key = '<your apu key>'
integration_data_csv = './integrationList.csv' # set this to your desired path or leave the same to generate csv in same directory
api_headers = {'Content-Type': 'application/json','Authorization':'GenieKey ' + api_key}
list_integration_url = "https://api.opsgenie.com/v2/integrations/" 
expand_params = {'expand': 'contact'}


def build_integration_list(api_key, url, api_headers):
    integration_list_request = requests.get(url = list_integration_url, headers = api_headers)
    integration_list = json.loads(integration_list_request.text) 
    return integration_list

# def generate_csv(integrations):
#     df = pd.DataFrame(integrations)
#     df_transposed = df.transpose()
#     df_transposed.to_csv(integration_data_csv, sep=',', encoding='utf-8')

def generate_csv(integrations):
    print(integrations[0])
    keys = integrations[0].keys()
    with open(integration_data_csv, 'w', newline='')  as output_file:
	    dict_writer = csv.DictWriter(output_file, keys)
	    dict_writer.writeheader()
	    dict_writer.writerows(integrations)

integrations = build_integration_list(api_key, list_integration_url, api_headers)
generate_csv(integrations)

