import os
import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-target', '-t', required=True, help='Enter the base URL - https://example.service-now.com.')
parser.add_argument('-user', '-u', required=True, help='Enter the username.')
parser.add_argument('-password', '-p', required=True, help='Enter the password.')
args = parser.parse_args()

url = args.target
user = args.user
pwd = args.password

snurl = url + '/api/now/table/'
headers = {"Accept":"application/json"}
 
importtables = open('tables.txt','r')
tables = importtables.read().splitlines() 

for t in tables:
    fullurl = snurl + t
    r = requests.get(url)
    response = requests.get(fullurl, auth=(user, pwd), headers=headers)
    print('Attempting to dump: ' + t)
    data = response.json()

    with open(t+'.txt','w') as write_file:
        json.dump(data, write_file)
    
importtables.close()
