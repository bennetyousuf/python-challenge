# python-challenge 

Student Assignment creating Python script to analyze financial and voting data csvs and return results from analysis in text file output.  

## Background ##

In this homework assignment, you'll be using the concepts you've learned to complete the two Python Challenges, PyBank and PyPoll.
Both of these challenges encompass a real-world situation where your newfound Python scripting skills can come in handy. These challenges are far from easy so expect some hard work ahead! 

Inside your local git repository, create a directory for each Python Challenge. Use folder names corresponding to the challenges: PyBank and  PyPoll.
Inside of each folder that you just created, add the following:
  - A new file called main.py. This will be the main script to run for each analysis.
  - A "Resources" folder that contains the CSV files you used. Make sure your script has the correct path to the CSV file.
  - An "analysis" folder that contains your text file that has the results from your analysis.
  - Push the above changes to GitHub or GitLab. 

## Pybank ## 

In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:
  1. The total number of months included in the dataset
  2. The net total amount of "Profit/Losses" over the entire period
  3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
  4. The greatest increase in profits (date and amount) over the entire period
  5. The greatest decrease in losses (date and amount) over the entire period
  6. In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## PyPoll ## 

In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
  1. The total number of votes cast
  2. A complete list of candidates who received votes
  3. The percentage of votes each candidate won
  4. The total number of votes each candidate won
  5. The winner of the election based on popular vote.
  6. In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## Hints and Considerations ## 
  1. Consider what we've learned so far. To date, we've learned how to import modules like csv; to read and write files in various formats; to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and to debug along the way. Using what we've learned, try to break down your tasks into discrete mini-objectives. This will be a much better course of action than spending all your time looking for a solution on Stack Overflow. 
 
  2. As you will discover, for some of these challenges, the datasets are quite large. This was done purposefully, as it showcases one of the limits of Excel-based analysis. While our first instinct, as data analysts, is often to head straight into Excel, creating scripts in Python can provide us with more robust options for handling "big data". 
   
  3. Write one script for each dataset provided. Run your script separately to make sure that the code works for its respective dataset.
  
  4. Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file

