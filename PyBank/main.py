import os
import csv

# Path to collect data from Pybank
Pybank = os.path.join("..", "Pybank", "Resources", "budget_data.csv")
count = 0

#def summary (Pybank): 
    #profit_loss = int(Pybank[1])
    #total = 0
    #total = sum(profit_loss)
with open(Pybank, 'r') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    header = next(csv_reader)
    total = 0
    for row in csv_reader:
        count += 1
        total += int(row[1])
print('Financial Analysis')
print ('Total Month:',count) 
print ('Total:', total)

#with open(Pybank, 'r') as count_file:
   # csv_reader = csv.reader(count_file)
    #csv_header = next(csv_reader)
    #for row in csv_reader:
        #count += 1
#print (count)

#print('Pybank lives at:', Pybank)

#def summary(Pybank):
#date = str(Pybank[0])
    #return (len(date))
    #profit_loss = int(Pybank[1])
    #Sum_months = len(1 for row in PyPoll)
    
#def summary(Pybank):
    #profit_loss = int(Pybank[1])
    #Sum = sum(profit_loss)
    #print(Sum)

    
    #print(csvreader)
    #csv_header = next(csvreader)
    #print(csv_header)

        