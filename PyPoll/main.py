import os

import pandas as pd

import csv


csvpath = os.path.join('/Users/hulls/Desktop/GitHub/Python-challenge/python-challenge/PyPoll/Resources', 'election_data.csv')

poll_data_df = pd.read_csv(csvpath)


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


vote_count = poll_data_df["Candidate"].value_counts()

percentages = poll_data_df["Candidate"].value_counts(normalize=True).mul(100).round(3).astype(str) + '%'

#print(f"{percentages}")

#print(f"{vote_count}")

winner = poll_data_df["Candidate"].value_counts().idxmax()

#print(f"{winner}")


print(f"Election Results")

print(f"---------------------------------")

print(f"Total Votes: {(len(total_votes))}")

print(f"---------------------------------")

print(f"{candidate_list[0]}: {percentages[0]} ({vote_count[0]})")

print(f"{candidate_list[1]}: {percentages[1]} ({vote_count[1]})")

print(f"{candidate_list[2]}: {percentages[2]} ({vote_count[2]})")

print(f"{candidate_list[3]}: {percentages[3]} ({vote_count[3]})")

print(f"---------------------------------")

print(f"Winner: {winner}")

print(f"---------------------------------")