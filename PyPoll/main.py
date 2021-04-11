import os 

#import CSV
import csv

csvpath =os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')
#print(csvpath)
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    #print(csvreader)

    csv_header = next(csvreader)

    #set all variables for outputs, rowcount set to ze
    rowcount = 0
    unique_candidates = []
    candidate_list=[]
    
    #to find total nunber of votes cast, row count of Voter ID  
    for row in csvreader:
        #to find total number of votes cast
        rowcount+=1  

        # Find complete list of candidates who received votes. To find unique number of candidates, set unique_candidates to an empty list first (done above). Then write a conditional statement if column 3 (index 2) is not in the list of unique_candidtes, then append  
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])

        #To find a comprehensive list of candidates
        candidate_list.append(row[2])

#create a dictionary to hold the key for each unique candidate and the values for each one. Set value of each key (unique candidates) to zero since we will be counting using or loop below
#note: candidate_list variable does not exist until after the for loop (for row in csvreader:) and is meant to be a comprenhensive/non-distinct list of values in index 2 of the variable row. We can now create a new for loop.
unique_candidates_dict= dict.fromkeys(unique_candidates,0)
for candidate in candidate_list:

    unique_candidates_dict[candidate]+= 1

#print(unique_candidates_dict) 

#to set variable to help count winning number of votes so we can find winning candidate name  using for loop
winning_number_votes = 0


#to dynamically access unique candidate name from the dictionary, using .items at the end of the of the dictionary is what allows yo uto call 2 variables (final_candidate and number_of_votes) in the for loop
for final_candidate, number_of_votes in unique_candidates_dict.items():
    #to print final answers: print final_candidate    
    #print(f'{final_candidate}: {round(((number_of_votes/rowcount)*100),3)}% ({number_of_votes})')

    #to find candidate name with winning number of votes    
    if number_of_votes > winning_number_votes:
        winning_number_votes =number_of_votes
        #to find winning candidate, as we loop through final_candidate and number_of_votes variables in unique_candidates dictionary, if numvber_of_votes is greater than winning_number of then the value of winning_nummber of votes at that point in the loop is equal to your number_votes
        #once the loop has completed going throuhg the final_candidates and number_of_votes in the dictionary, then your winning_candidate will be equal to the final_candidate key  that is aligned with numvber_of_votes value that winning_numbeer_of_votes was set to
        winning_candidate = final_candidate

#Print winnning candidate        
#print(f'Winner: {winning_candidate}')
    
    





#Print Election Results Final Values

print('Election Results') 
print('________________________') 
print('Total Votes: ',rowcount) 
print('________________________') 
for final_candidate, number_of_votes in unique_candidates_dict.items():
    #to print final answers: print final_candidate    
    print(f'{final_candidate}: {round(((number_of_votes/rowcount)*100),3)}% ({number_of_votes})')

print('________________________') 
print(f'Winner: {winning_candidate}')
print('________________________')  

#Write to text file for multiple lines
Election_Results_File = open("Election Results.txt", "w+")
Election_Results_File.write(f""" Election Results
________________________
Total Votes: {rowcount}
________________________
""")
for final_candidate, number_of_votes in unique_candidates_dict.items():
    #to print final candidate information into file without writig in the for loop 
    #use \n to move teh final candidates and their stats to be written onto new lines
    Election_Results_File.write(f'{final_candidate}: {round(((number_of_votes/rowcount)*100),3)}% ({number_of_votes})\n')
Election_Results_File.write(f"""________________________
Winner: {winning_candidate}
________________________""")


