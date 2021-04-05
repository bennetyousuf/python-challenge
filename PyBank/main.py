import os 

#import CSV
import csv

csvpath =os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    print(csvreader) 

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}") 

#row counter, total number of rows in the column “Date” output as “Total Months” is desired final output
    rowcount = 0
    for row in csvreader:
        rowcount += 1
    print('Total Months: ',rowcount)

#Calculate the total of "Profit/Losses" over Period
    row_sum = sum('Profits',86) 
    


    
    
    
   # for row in csvreader:
        #len(row)
        #row=len(row)+=1
        #print(row)






