import os

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

import csv

with open(csvpath) as poll_data:

    csvreader = csv.reader(poll_data, delimiter=',')

    csv_header = next(csvreader)

    print(poll_data)