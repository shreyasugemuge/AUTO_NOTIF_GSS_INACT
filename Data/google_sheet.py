# AUTO_NOTIF_GSS_INACT
# Author: Shreyas Ugemuge

from oauth2client.service_account import ServiceAccountCredentials

import gspread
from Config import sheets_api as const


def fetch(sheet_name):
    # use creds to create a client to interact with the Google Drive API
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'Data/client_secret.json', const.SCOPE)
    client = gspread.authorize(creds)
    return client.open(sheet_name).sheet1


def write(row, column, data, sheet):
    sheet.update_cell(row, column, data)
    print(row, column, data)
