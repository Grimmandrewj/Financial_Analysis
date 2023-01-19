# Instructions
    # Create a script that returns the following: 
        # The total number of votes cast
        # A complete list of candidates who received votes
        # The percentage of votes each candidate won
        # The total number of votes each candidate won
        # The winner of the election based on popular vote.

# Import os and csv modules for directory convention and reading the .csv file
import os
import csv

# Set variables for desired data
total_votes = 0
candidate = ""
final_tally = {}
winner_votes = 0
winner_name = ""


# Set Variable for path for reading .csv file and writing to .txt file
csvpath = os.path.join('Resources', 'election_data.csv')
text_output = os.path.join('Analysis', 'election_analysis.txt')

# Open .csv file for reading
with open(csvpath) as csvfile:

    # Utilize csv module and reader function to read .csv file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip over header row to begin reading data
    csv_header = next(csvreader)

    # Set for loop to read through .csv file
    for row in csvreader:

        # Tally values in Ballot ID column to find total number of votes
        total_votes += 1

        # Looping through candidates and adding their vote counts to dictionary
        candidate = row[2]
        if candidate in final_tally:
            final_tally[candidate] += 1
        else:
            final_tally[candidate] = 1

# Print initial results in terminal
print("Election Results")
print("-------------------")
print(f"Total Votes: {total_votes}")
print("-------------------")

# Print initial results to text file
txt_output1 = (
    f"Election Results\n"
    f"--------------------\n"
    f"Total Votes: {total_votes}\n"
    f"--------------------\n"
    )
with open(text_output, "w") as txt_file:
    txt_file.write(txt_output1)

# Calculating percentage of votes and printing values in requested format
for candidate in final_tally:

    percentage = (final_tally[candidate] / total_votes) * 100
    perc_format = "{:.3f}".format(percentage)

    print(candidate + ": " + str(perc_format) + "%" + " (" + str(final_tally[candidate]) + ")") 
    
    # Printing new data to text file
    txt_output2 = (f"{candidate} : {perc_format}% ({final_tally[candidate]})\n")

    # Calculate winning candidate with highest popular vote count
    if final_tally[candidate] > winner_votes:
        winner_votes = final_tally[candidate]
        winner_name = candidate

    # Appending text file with new calculations
    with open(text_output, "a") as txt_file:
        txt_file.write(txt_output2)

# Print final data results to text file 
txt_output3 = (
    f"-------------------\n"
    f"Winner: {winner_name}\n"
    f"-------------------\n"
    )

# Print final data results to terminal
print(txt_output3)

# Appending text file with final data
with open(text_output, "a") as txt_file:
    txt_file.write(txt_output3)




