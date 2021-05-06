import os
import csv

PyPoll = os.path.join("..", "PyPoll", "Resources", "election_data.csv")
print('PyPoll lives at:', PyPoll)


def vote_counts(PyPoll):
    Voter_ID = str(PyPoll[0])
    County = str(PyPoll[1])
    Candidate = str(PyPoll[2])
    
with open(PyPoll, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',',)