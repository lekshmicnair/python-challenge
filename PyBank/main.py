import csv
import os

#File location
csvpath=os.path.join ('./Resources', 'budget_data.csv')

#Read File
with open(csvpath) as csv_file:
    csvreader= csv.reader(csv_file, delimiter=',')
    csv_header=next(csvreader)
    for row in csvreader:
        print row[0], row[1]