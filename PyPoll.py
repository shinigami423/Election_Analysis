# election results by importing csv and using 'os' when the direct path is unknown
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Initialize a total vote counter
total_votes = 0

# Candidate options///setting it as a list to find candidate names
candidate_options = []          #used in for loop to check if candidate has been counted

# Create disctionary to link candidates(keys) to their votes(values)
candidate_votes = {}            

# Winning Candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
# Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the csv file
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row. index 2 because we want the 3rd column
        candidate_name = row[2]

        # Add the candidate name to the candidate list if the candidate does not match any existing canididate.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count thru dictionary
            candidate_votes[candidate_name] = 0     #this is where we assign keys-values in the dictionary
            
        # Add a vote to that candidat's count
        candidate_votes[candidate_name] += 1


    # Printing results using the list of keys in the dictionary and assign the list of 'votes' to the values
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]         #set votes(value) from candidate_vote(dictionary)
        
        # The percentage of votes each candidate won
        vote_percentage = round(float(votes)/float(total_votes)*100, 1)
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        # The total number of votes each candidate won
        #print(f"{candidate_name}: received {votes} votes.")


# Determine if votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #set votes to winning_count///for each index in the list
            winning_count = votes
            #set votes to winning_percetange///for each index in the list
            winning_percentage = vote_percentage
            #set winninng_candidate to the candidate's name
            winning_candidate = candidate_name
        
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# Print electrion result
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winning: {winning_candidate}\n"
        f"Wiinning Vote Count: {winning_count:,} votes\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)











# Write data to the file
#    txt_file.write("Counties in the Election\n----------------------------\nArapahoe\nDenver\nJefferson")

