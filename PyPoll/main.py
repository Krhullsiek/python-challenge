import os
import pandas as pd
import csv

csvpath = os.path.join('/Users/hulls/Desktop/GitHub/Python-challenge/python-challenge/PyPoll/Resources', 'election_data.csv')

with open(csvpath) as poll_data:

    csvreader = csv.reader(poll_data, delimiter=',')

    csv_header = next(csvreader)

    total_votes = []
    candidate_list = []
    vote_count = []

    for row in csvreader:

        total_votes.append(str(row[0]))

        candidate = str(row[2])


        if candidate not in candidate_list:
            candidate_list.append(candidate)

#print(f"List of candidates: {candidate_list}")

khan_votes = candidate.count(candidate_list[0])
correy_votes = candidate.count(candidate_list[1])
li_votes = candidate.count(candidate_list[2])
otooley_votes = candidate.count(candidate_list[3])

    


print(f"Total Votes: {(len(total_votes))}")
print(f"v: {candidate_list[0]} {khan_votes}")
print(f"v: {candidate_list[1]} {correy_votes}")
print(f"v: {candidate_list[2]} {li_votes}")
print(f"v: {candidate_list[3]} {otooley_votes}")



