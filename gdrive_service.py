import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = './client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

# Get the list of available cars
def get_cars():
    #Fetch the sheet
    sheet = client.open('Décompte Point Simracing').worksheet("Voitures")
    return sheet.get_all_records()

# Update "Résultats" sheet with ACSM live timings data
def set_results(results):
    sheet = client.open('Décompte Point Simracing').worksheet("Résultats")
    index = 2

    if sheet.row_count > 1:
        sheet.batch_clear(['A2:H' + str(sheet.row_count)])

    for res in results:
        sheet.insert_row(list(res.values()), index)
        index += 1


