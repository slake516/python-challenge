
#Resources used:  Jtuttle314 Github
# Dependencies
import csv
import os

# Files to Load

file_to_output = "budget_analysis.txt"

# Variables to Track
total_months = 0
total_revenue = 0

prev_revenue = 0

greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

revenue_changes = []

# Read Files
with open("budget_data.csv") as revenue_data:
    reader = csv.DictReader(revenue_data)

    # Loop through all the rows of data we collect
    for row in reader:
        
         # Keep track of changes
        if(total_months==0):
            revenue_change = 0
            else:
                revenue_change = int(row["Profit/Losses"]) - (prev_revenue)
           
            
#             print(revenue_change)

        # Calculate the totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
        # print(row)

        # Keep track of changes
#         revenue_change = int(row["Profit/Losses"]) - prev_revenue
#         revenue_change= revenue_change 
#         print(revenue_change)
        
        # Reset the value of prev_revenue to the row I completed my analysis
        prev_revenue = int(row["Profit/Losses"])
        print(prev_revenue)

        # Determine the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]

        # Add revenue changes to the revenue_changes list
        revenue_changes.append(revenue_change)
        #revenue_changes.remove([0])

    # Set the Revenue average
    revenue_avg = sum(revenue_changes) /len(revenue_changes)
    
    # Show Output
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    


# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
