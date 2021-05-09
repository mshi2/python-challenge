import os
import csv

# Path to collect data from Pybank
Pybank = os.path.join("..", "Pybank", "Resources", "budget_data.csv")

#Lists
profit_loss = []
months = []
monthly_changes = []
month_count = 0
total_profits = 0
first_month = 0
total_monthly = 0
with open(Pybank, 'r') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    header = next(csv_reader)
    
    for row in csv_reader:
        month_count += 1
        total_profits += int(row[1])
        #store months in list
        months.append(row[0])
        #store profit_loss in list
        profit_loss.append(row[1])
        
        #average change from month to month
        next_month = int(row[1])
        monthly_change = next_month - first_month
        #store monthly change to list profit_loss
        monthly_changes.append(monthly_change)
        #total monthly_change profits
        total_monthly = total_monthly + monthly_change
        first_month = next_month
        average_monthly_change = (total_monthly/month_count)
        greatest_increase = max(monthly_changes)
        greatest_decrease = min(monthly_changes)
        date_max = months[monthly_changes.index(greatest_increase)]
        date_min = months[monthly_changes.index(greatest_decrease)]
print("Financial Analysis")
print(f"Total Month: {month_count}") 
print(f"Total Profits:${total_profits}")
print(f"Average Change: ${round(average_monthly_change,2)}")
print(f"Greatest Increase in Profits:${greatest_increase} on {date_max}")
print(f"Greatest Decrease in Profits:${greatest_decrease} on {date_min}")

# Create a text file with the results
output_file = 'Analysis/financial_analysis.txt'
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow("Financial Analysis")
    csvwriter.writerow(f"Total Months: {month_count}")
    csvwriter.writerow(f"Total: ${total_profits}")
    csvwriter.writerow(f"Average Change: ${round(average_monthly_change,2)}")
    csvwriter.writerow(f"Greatest Increase in Profits: ${greatest_increase} on {date_max}")
    csvwriter.writerow(f"Greatest Decrease in Profits: ${greatest_decrease} on {date_min}")
