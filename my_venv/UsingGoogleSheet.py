# importing pandas
import pandas as pd

# importing gspread
import gspread

gc = gspread.service_account(filename="C:\\Users\\ACER\\Downloads\\shining-chain-412715-b8a45c54dceb.json")

sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/196ibVvJAK5GN2RrWmo0ZdpdtlAgG4DywnbGmNyFlcdo/edit?usp=sharing")

ws = sheet.worksheet("Name1")

df = pd.DataFrame(ws.get_all_records())
print(df)
