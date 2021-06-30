# election results by importing csv and using 'os' when the direct path is unknown
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
# Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    print(headers)




# Now open it using the with statement open the file as a text file///////////// DON'T NEED TO USE THE OPEN() OR CLOSE() FUNCTIONS
#with open(file_to_save,"w") as txt_file:

# Write data to the file
#    txt_file.write("Counties in the Election\n----------------------------\nArapahoe\nDenver\nJefferson")



# 1. The total numb of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the elctrion base on popular vote.





