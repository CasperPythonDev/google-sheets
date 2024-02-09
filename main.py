import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "10L5wBWHf1KR4QP9c8I6NTHCEDW_QKn_IAAriSg7uc2c"
sheet = client.open_by_key(sheet_id)

value_list_col = sheet.sheet1.col_values(1)
value_list_row = sheet.sheet1.row_values(1)
print(f"column 1: {value_list_col}")
print(f"row 1: {value_list_row}")
