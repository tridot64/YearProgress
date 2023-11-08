import os

try:
    from datetime import date
    from datetime import timedelta
    from pathlib import Path
    import tkinter
except ImportError as e:
    os.system(r'''pip install datetime pathlib tkinter''')

os.system(r'''mkdir %HOMEDRIVE%%HOMEPATH%\\AppData\\Local\\YearProgress ''')
os.system(r'''copy YearProgress.exe %HOMEDRIVE%%HOMEPATH%\\AppData\\Local\\YearProgress ''')
os.system(r'''Powershell -Command "& { Start-Process "\"schtasks.exe\"" -ArgumentList @(\"/create\",\"/sc\",\"ONLOGON\",\"/tn\",\"YearProgress\",\"/tr\",\"$HOME\\AppData\\Local\\YearProgress\\YearProgress.exe\") -Verb RunAs } " ''')


minus_1 = timedelta(days = 1)
today = date.today()
yester = today - minus_1
yester_str = yester.strftime("%d/%m/%y")

with open(str(Path.home())+"\\AppData\\Local\\YearProgress\\curr_date.txt", "w+") as f:
    f.write(yester_str)



