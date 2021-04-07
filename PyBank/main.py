#First we must import our csv file and import it

import os

csvpath = os.path.join('c:/Users/hulls/Desktop/GitHub/Python-challenge/python-challenge/PyBank/Resources', 'budget_data.csv')

import csv

#Now we can pull the headers from our csv file to use in our code and skip the header when looking at the collumn values

with open(csvpath) as bank_data:

    csvreader = csv.reader(bank_data, delimiter=',')

    csv_header = next(csvreader)

#We need to create an empty list for total_months, total_profits, monthly_change

    total_months = []
    
    total_profit = []
    
    monthly_change = []

    #Look inside the rows in our open csv

    for row in csvreader:

        #We need to add values within the rows from column 0 to our empty list for total_months
       
        total_months.append(str(row[0]))
        
        #We need to add values within the rows from column 1 to our empty list for total profit

        total_profit.append(int(row[1]))

    #now we need to use a variable (x) to retrieve our total_profit list values
    
    for x in range(1, len(total_profit)):

        #We need to take one value in the list and subtract by the row before it to find the change in the value, and add that to our monthly_change list

        monthly_change.append((int(total_profit[x]) - int(total_profit[x-1])))
    
        #test this is working properly

        #print(f"{monthly_change}")
    
    #We need to find the average monthly changes in profit, so we add the changes and divide by number of months

    average_profit_change = sum(monthly_change) / len(total_months)
        
    #print(f"{average_profit_change}")

    #We can use our monthly change list to find max change

    greatest_increase = max(monthly_change)

    #print(f"{greatest_increase}")

    #We can use our monthly change list to find min change

    greatest_decrease = min(monthly_change)

    #print(f"{greatest_decrease}")

    #We need to find the value of the row next to the max increase to show the month it happened in, we can use index for this

    i = monthly_change.index(greatest_increase)
    greatest_increase_month = total_months[i+1]

    #print(f"{i} {greatest_increase_month}")

    #We need to find the value of the row next to the max decrease to show the month it happened in, we can use index for this

    d = monthly_change.index(greatest_decrease)
    greatest_decrease_month = total_months[d+1]
    
    #print(f"{d} {greatest_decrease_month}")

    #print the results

    print("Financial Analysis")
    
    print("-------------------------------------------")
    
    print(f"Total Months: {(len(total_months))}")
    
    print(f"Total: ${sum(total_profit)}")
    
    print(f"Average Change: ${round(average_profit_change, 2)}")
    
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


