import os 

#import CSV
import csv

csvpath =os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    #print(csvreader) 

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}") 

#set all variables and lists that need to be set and will use the for row in csv reader for loop
#rowcount set to 0 and  uses for loop to help count total numbre of months
#total_profit set to 0 and uses for loop to calculate total profit as loop iterates through index 1 and adds to it as loop continues
#change_profit and monthly_change_profit set as empty lists 

    rowcount = 0
    total_profit = 0
    months = []
    change_profit = []
    monthly_profit_change= []
        
    for row in csvreader:
     #to count total number of months, add one as the loop iterates through rows
        rowcount += 1
        
    #to calculate total profit
        total_profit += int(row[1]) 
    
    #to calculate average change in differences 
    #create list that shows all values of months and all values of profit/losses
        months.append(row[0])
        change_profit.append(int(row[1]))

    #creating for loop with an index value to fnd the next value +1 as we loop through months and profit/losses to append values
    #len function defines all values in the change_profit
    # column (86) but since running difference starts at row 2 (row 2-1) then subtract one row from total len
    for i in range(len(change_profit)-1):

    #function below subtracting the difference between the second value in 'Profit/Loss' i+1  and first value i
        total_change_profit=change_profit[i+1]-change_profit[i]
        monthly_profit_change.append(total_change_profit)

#find average of profit loss over time
round(sum(monthly_profit_change)/len(monthly_profit_change),2)  

#find min and max average monthly change in profit 
max(monthly_profit_change)
min(monthly_profit_change)

#find max and min month of monthly_profit_changes. .index used to find the index location of largest change. Since monthly_profit_change has 85 rows (since it begins on row 2 after taking the difference of the first 2 values) and the original column "Date" has 86 values, we add +1 to the index to compensate for difference in row numbers
max_monthly_profit_change = monthly_profit_change.index(max(monthly_profit_change))+1
min_monthly_profit_change = monthly_profit_change.index(min(monthly_profit_change))+1


#print stats in main.py file

print('Financial Analysis') 
print('________________________') 
print('Total Months: ',rowcount)  
print('Total: ', str(total_profit))
print('Average Change : $',str(round(sum(monthly_profit_change)/len(monthly_profit_change),2))) 
print('Greatest Increase in Profits:',months[max_monthly_profit_change],' ($',max(monthly_profit_change),')')
print('Greatest Decrease in Profits:',months[min_monthly_profit_change],' ($',min(monthly_profit_change),')') 

#write output file to .txtfile 
#attempt to open file "Financial_Analysis.txt", does not exists so will create with read/write ability
#write stats into the file "Financial_Analysis.txt" that was just created

Financial_Analysis_File = open("Financial_Analysis.txt", "w+")
Financial_Analysis_File.write(f""" Financial Analysis
________________________
Total Months: {rowcount}  
Total:  {total_profit}
Average Change : $ {(round(sum(monthly_profit_change)/len(monthly_profit_change),2))}
Greatest Increase in Profits: {months[max_monthly_profit_change]} (${max(monthly_profit_change)})
Greatest Decrease in Profits: {months[min_monthly_profit_change]} (${min(monthly_profit_change)})

""")
