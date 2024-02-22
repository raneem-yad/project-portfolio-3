import gspread
from google.oauth2.service_account import Credentials
	
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# The same name as your sheets are 
SHEET = GSPREAD_CLIENT.open('TaskTrack')
def get_sheet():
    return SHEET