# Instructions
    # Create a script that returns the following:
        # The total number of months included in the dataset
        # The net total amount of "Profit/Losses" over the entire period
        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        # The greatest increase in profits (date and amount) over the entire period
        # The greatest decrease in profits (date and amount) over the entire period

# Import os and csv modules for directory convention and reading the .csv file
import os
import csv

# Set variables for desired data
months = []
total_months = 0
total = []
net_total = 0
amount = []
change = []
difference = 0
total_difference = 0
average_change = 0
great_incr = 0
great_decr = 0


# Set Variable for path to .csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open .csv file for reading
with open(csvpath) as csvfile:

    # Utilize csv module and reader function to read .csv file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip over header row to begin reading data
    csv_header = next(csvreader)

    # Set for loop to read through .csv file
    for row in csvreader:

        # Add values in Date column to list and find length to determine total number of months
        months.append(row[0])
        total_months = len(months)

        # Add cumulative sum of Profit/Losses column to obtain net total
        total.append(int(row[1]))
        net_total = sum(total)

    # Calculate and log changes in profit/loss
    for i in range(len(total) - 1):
        change.append(total[i+1] - total[i]) 

    # Calculate average change in profit/loss
    average_change = round(sum(change) / len(change), 2)

    # Calculate greatest increase and decrease in period
    great_incr = max(change)
    great_decr = min(change)

    # Use index to obtain months with greatest increase and decrease
    month_increase = change.index(max(change)) + 1
    month_decrease = change.index(min(change)) + 1
       
    # Print the calculated values to terminal
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: ", total_months)
    print(f"Net Total: $", net_total)
    print(f"Average change: $", average_change)
    print(f"Greatest Increase in Profits: {months[month_increase]} (${(str(great_incr))})")
    print(f"Greatest Decrease in Profits: {months[month_decrease]} (${(str(great_decr))})")

    # Print calculated values to text document
    output = os.path.join("Analysis/financial_analysis.txt")
    with open(output, "w") as new:
        new.write("Financial Analysis")
        new.write("\n")
        new.write("---------------------------")
        new.write("\n")
        new.write("Total Months: " + str(total_months))
        new.write("\n")
        new.write("Net Total: $" + str(net_total))
        new.write("\n")
        new.write("Average change: $" + str(average_change))
        new.write("\n")
        new.write(f"Greatest Increase in Profits: {months[month_increase]} (${(str(great_incr))})")
        new.write("\n")
        new.write(f"Greatest Decrease in Profits: {months[month_decrease]} (${(str(great_decr))})")


  
    






        


    