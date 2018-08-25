PyBank folder
import csv
import os 

csv_file= os.path.join("budget_data.csv")
file_to_output = ("budget_data.txt")




# Track Various Revenue Parameters
total_months = 0
total_revenue = 0 
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

with open(csv_file, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    next(csvreader)




        
    for row in csvreader:
        
        #track the total months
        total_months = total_months + 1 
        
        # track the total revenue
        total_revenue = total_revenue + int(row[1])
        
        #figure out the revenue changes
        
        revenue_change = int(row[1]) - prev_revenue
        prev_revenue = int(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row[0]]
        
        #calculate the largest increase
        if(revenue_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change
            
        #Calculate the largest decrease 
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_change
        
    #calc the avg    
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)   

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")     
        
print(output) 

with open(file_to_output,"w") as txt_file:
  txt_file.write(output)
