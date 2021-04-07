#We need to import the csv file and module for pandas

import os

import pandas as pd

import csv


csvpath = os.path.join('/Users/hulls/Desktop/GitHub/Python-challenge/python-challenge/PyPoll/Resources', 'election_data.csv')

#We need to have pandas open read csv file

poll_data_df = pd.read_csv(csvpath)

#We need to set open csv file as reader and grab headers

with open(csvpath) as poll_data:

    csvreader = csv.reader(poll_data, delimiter=',')

    csv_header = next(csvreader)

    #Within our open csv file we need to create lists for total votes, cadidate list and vote count

    total_votes = []

    candidate_list = []

    vote_count = []

    #Within our rows, we want to take the values of collumns 0 and return it to the list for total votes

    for row in csvreader:

        total_votes.append(str(row[0]))

        #We want to say that candidate values are the rows within column 2
        candidate = str(row[2])

        #We want to say that if our value of candidate that we look at in the 1st row of this column is not in our candidate list, 
            # then add it to the candidate list (so we don't get duplicate names). It will do this for each row, and skip the duplicates.
        if candidate not in candidate_list:
           
            candidate_list.append(candidate)

#Test that this worked

#print(f"List of candidates: {candidate_list}")

#We can use the pandas module to find how many times a candidate value is listed, which shows the number of votes for that candidate

vote_count = poll_data_df["Candidate"].value_counts()

#We can use the pandas module to find the percentage of counts for each candidate, and use formatting so it will print the way we want it later

percentages = poll_data_df["Candidate"].value_counts(normalize=True).mul(100).round(3).astype(str) + '%'

#print(f"{percentages}")

#print(f"{vote_count}")

#We can use pandas module to find the candidate with the max amount of times their name is listed to show the winner

winner = poll_data_df["Candidate"].value_counts().idxmax()

#print(f"{winner}")


#print the results

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