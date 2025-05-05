from pathlib import Path
import matplotlib.pyplot as plt
import csv
from datetime import datetime
# This program reads a CSV file containing unemployment data and plots it using matplotlib.

path = Path('OHUR (1).csv')
lines = path.read_text(encoding='utf-8').splitlines()
#iterable obj to process each line

reader = csv.reader(lines)
header_row = next(reader)
# print(header_row)

for index, col_title in enumerate(header_row): #analyses the data and gives the index and title of each column
    print(f'{index} {col_title}, ' , end=' ')

dates = []   
unemployment_rate = []

for row in reader:
    current_date = datetime.strptime(row[0], '%Y-%m-%d')
    date = current_date
    unemployment = float(row[1])
    dates.append(date)
    unemployment_rate.append(unemployment)

 # graphing the processed data

plt.style.use('dark_background')
figure, graph = plt.subplots()
graph.plot(dates, unemployment_rate, color= 'magenta')
plt.show()   
    





