## Goal
- In this challenge I was provided with two datasets (PyBank and PyPoll):
  - One outlined financial data which included month, year, and whether there was a reported profit or loss
  - The other outlined election results which included Ballot ID, County, and the Candidate for which the vote was cast
- For the financial dataset, I was tasked with calculating and printing data to the terminal and a text file including the following:
  - Total number of months included in the dataset
  - Net total of profits and losses recorded
  - The changes in profits and losses during this period and the average of the changes
  - The greatest increase and decrease recorded and in which month/year they occurred
- For the election dataset, I was tasked with calculating and printing the following:
  - Total number of votes cast
  - A complete list of the candidates who received votes
  - The percentage of and total of votes each candidate received
  - The winner of the election based on the popular vote

## Method
- For both datasets, I set variables for the desired data to be recorded as strings, integers, in lists, and in dictionaries as appropriate
- For the financial dataset:
  - I calculated and printed the total number of rows (showing months)
  - I looped through the data to record and print the changes in profit and losses, calculated the average difference, and determined the greatest increase and decrease
- For the election dataset:
  - I looped through the data and tallied the rows to determine total votes cast
  - During the loop, I captured each candidate name and the amount of votes cast for them
  - I then calculated the percentage of votes and the winning candidate with the most popular votes
  
## Summary and Results
- Both analyses can be found in their respective folders in this repository (PyBank/Analysis/financial_analysis.txt, and PyPoll/Analysis/election_analysis.txt)

- In the financial dataset, there were 86 months recorded, a net total of profit and losses of $22,564,198, and an average change of $8,311.11, with the greatest increase recorded in August 2016 ($1,862,002), and the greatest decrease in February 2014 (-$1,825,558):

![image](https://user-images.githubusercontent.com/120341249/213341718-723a2aa6-fc65-4dc0-9bb1-d5465df8d3fe.png)
- In the election dataset, the total votes cast was 369,711, candidate Charles Casper Stockham received 23.048% of the votes (85,213), Diana DeGette received 73.812% of the votes (272,892), and Raymon Anthony Doane received 3.139% of the vote (11,606).  The winning candidate was Diana DeGette:

![image](https://user-images.githubusercontent.com/120341249/213342025-abf653aa-0ebf-42c1-bdda-774418a778fa.png)

