import csv
import re

with open("/home/guibax/PycharmProjects/Fito/gas_control/gas_data.txt", "r") as csvfile:
    plots = csv.reader(csvfile, delimiter='\t')
    date = []
    ars = []
    h2 = []
    he = []

    for row in plots:
        row[0] = re.sub('/2018', '', row[0])
        date.append(row[0])
        ars.append(int(row[1]))
        h2.append(int(row[2]))
        he.append(int(row[3]))
