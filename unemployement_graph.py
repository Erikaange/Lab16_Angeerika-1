# name: Lab16_Angeerika-1.py
# author: Angeerika
# comment: This program reads a CSV file containing unemployment data and plots it using matplotlib.
# date: 05/03/25



from pathlib import Path
import matplotlib.pyplot as plt
import csv
from datetime import datetime


path = Path('OHUR (1).csv')
lines = path.read_text(encoding='utf-8').splitlines()
#iterable obj to process each line

reader = csv.reader(lines)
header_row = next(reader)
# print(header_row)

for index, col_title in enumerate(header_row): #analyses the data and gives the index and title of each column
    print(f'{index} {col_title}, ' , end=' ')

# Prepare lists to store dates and unemployment rates
dates = []   
unemployment_rate = []


# Extract data from each row in the CSV
for row in reader:
    current_date = datetime.strptime(row[0], '%Y-%m-%d')
    date = current_date
    unemployment = float(row[1])
    dates.append(date)
    unemployment_rate.append(unemployment)

 # graphing the processed data
plt.style.use('ggplot')# Set the plot style
figure, graph = plt.subplots()
graph.plot(dates, unemployment_rate, color= 'magenta')# Plot dates (x-axis) against unemployment rates (y-axis)
graph.fill_between(dates, unemployment_rate, color='blue', alpha=0.2) #fill the area under the line

# Add title and axis label
graph.set_title('Unemployment Rate Timeline', fontsize=18)
graph.set_ylabel('Rates(%)', fontsize=16)
graph.set_xlabel('Date', fontsize=16)

figure.autofmt_xdate() #fix the date

plt.show()   # Display the plot

    





