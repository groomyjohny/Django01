
import csv

with open('process_cycles_very_light.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))