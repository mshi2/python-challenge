import os
import csv

PyPoll = os.path.join("..", "PyPoll", "Resources", "election_data.csv")
print('PyPoll lives at:', PyPoll)

candidates = {}
vote_count = []
total_votes = 0
vote_count = 0
with open(PyPoll, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',',)
    header = next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1
        
        #vote count per candidate
        candidate = row[2]
        #add to candidate list
        candidates.append(candidate)
        if candidate in candidates:
            candidate += 1
        else:
            candidate = 1
print(total_votes)
print(candidate)
