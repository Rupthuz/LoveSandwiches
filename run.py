import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT =gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():

    print("Please input a sales data from the last market")
    print("data should be six numbers, separeted by commas")
    print("examples: 10,20,30,40,50,60\n")

    data_str = input("Enter yout data here: ")
    print(f"the data provided if {data_str}")


get_sales_data()