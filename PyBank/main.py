import os

csvpath = os.path.join('c:/Users/hulls/Desktop/GitHub/Python-challenge/python-challenge/PyBank/Resources', 'budget_data.csv')

import csv


with open(csvpath) as bank_data:

    csvreader = csv.reader(bank_data, delimiter=',')

    csv_header = next(csvreader)

    
    total_months = []
    
    total_profit = []
    
    monthly_change =[]

    
    for row in csvreader:
       
        total_months.append(str(row[0]))
        
        total_profit.append(int(row[1]))

    
    for x in range(1, len(total_profit)):

        monthly_change.append((int(total_profit[x]) - int(total_profit[x-1])))

        #print(f"{monthly_change}")
    
    
    average_profit_change = sum(monthly_change) / len(monthly_change)
        
    #print(f"{average_profit_change}")

    greatest_increase = max(monthly_change)

    #print(f"{greatest_increase}")

    greatest_decrease = min(monthly_change)

    #print(f"{greatest_decrease}")

    i = monthly_change.index(greatest_increase)
    greatest_increase_month = total_months[i+1]

    #print(f"{i} {greatest_increase_month}")

    d = monthly_change.index(greatest_decrease)
    greatest_decrease_month = total_months[d+1]
    
    #print(f"{d} {greatest_decrease_month}")

    
    print("Financial Analysis")
    
    print("-------------------------------------------")
    
    print(f"Total Months: {(len(total_months))}")
    
    print(f"Total: ${sum(total_profit)}")
    
    print(f"Average Change: ${round(average_profit_change, 2)}")
    
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


