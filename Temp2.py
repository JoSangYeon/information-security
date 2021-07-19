import pandas as pd
import pygsheets
import time

gc = pygsheets.authorize(outh_file='client_secret.json')
print(gc)

file_name = '정보보안솔루션(응답)'

sh = gc.open(file_name)
sheet1 = sh.sheet1
data = sheet1.get_all_records()
data_len = len(data)
update = len(data)

print(data)
print(data_len)
while data_len == update:
    time.sleep(3)
    sh = gc.open(file_name)
    sheet1 = sh.sheet1
    data = sheet1.get_all_records()
    update = len(data)
    print("진행중...")
print(update)
print(data)