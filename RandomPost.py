import csv
import random

with open('top.csv','r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    number = random.randint(0,970)
    selected=[row for idx, row in enumerate(csv_reader) if idx in (number,number)]

print(selected[0][1]) #description of the website
print(selected[0][4]) #link of the website

