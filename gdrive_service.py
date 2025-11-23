import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os
from dotenv import load_dotenv

#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = './client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

load_dotenv()
gsheet_name =  os.getenv('GSHEET_NAME')

# Get the list of tracks
def get_tracks():
    #Fetch the sheet
    sheet = client.open(gsheet_name).worksheet("Circuits")
    return sheet.get_all_records()

# Get results
def get_results():
    sheet = client.open(gsheet_name).worksheet("Résultats")
    return sheet.get_all_records()
    
# Get last result
def get_last_result():
    sheet = client.open(gsheet_name).worksheet("Dernier résultat")
    return sheet.get_all_records()
    
# Get paliers
def get_paliers():
    sheet = client.open(gsheet_name).worksheet("Paliers")
    return sheet.get_all_records()

# Update "Résultats" sheet with ACSM result data
def set_results(results):
    sheet = client.open(gsheet_name).worksheet("Résultats")

    for res in results:
        sheet.insert_row(list(res.values()), 2)

# Update "Cumul" sheet
def set_pts(pts):
    sheet = client.open(gsheet_name).worksheet("Cumul")
    index = 2

    if sheet.row_count > 1:
        sheet.batch_clear(['A2:G' + str(sheet.row_count)])

    for d, pt in pts.items():
        print(pt)
        sheet.insert_row(list(pt.values()), index)
        
# Update "Dernier résultat" sheet
def set_last_result(last_result):
    sheet = client.open(gsheet_name).worksheet("Dernier résultat")
    sheet.insert_row(list(last_result.values()), 2)
        
