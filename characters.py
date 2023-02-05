import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Connect to Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("gs_credentials.json", scope)
client = gspread.authorize(credentials)

sheet = client.open("NewDatabase").sheet1
sheet_id = "1ZIqVRLdGF_bPcCGBCvUxaXwa6mEO6j8xgpt47_Gt-18"
sheet_name = "Characters"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url, on_bad_lines='skip')
df = df.fillna('')
sheet.update([df.columns.values.tolist()] + df.values.tolist())

class Char:
    def __init__(self):
        self.name = "I AM ERROR."
        self.hp = 10
        self.sp = 10
        self.atk = 0
        self.mag = 0
        self.dfn = 0
        self.res = 0
        self.spd = 0
        self.eva = 0
        self.acc = 0
        self.maxHp = self.hp
        self.maxSp = self.sp
        self.atkC = 0
        self.magC = 0
        self.dfnC = 0
        self.resC = 0
        self.spdC = 0
        self.evaC = 0
        self.accC = 0
        self.atkT = 0
        self.magT = 0
        self.dfnT = 0
        self.resT = 0
        self.spdT = 0
        self.evaT = 0
        self.accT = 0
        self.action = False
        self.KO = False
        self.passives = 0
        self.skills = 0


def base(self):
    self.maxHp = self.hp
    self.maxSp = self.sp
    self.atkB = 0
    self.magB = 0
    self.dfnB = self.dfn
    self.resB = self.res
    self.spdB = self.spd
    self.evaB = self.eva
    self.accB = 0


class Template(Char):
    def __init__(self):
        super().__init__()
        self.name = "I AM ERROR."
        self.fullname = "I AM ERROR"
        self.id = "000"
        self.hp = 10
        self.sp = 10
        self.dfn = 0
        self.res = 0
        self.spd = 0
        self.eva = 0
        self.passives = 2
        self.skills = 2
        base(self)
