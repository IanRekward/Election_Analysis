# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1.0 Initialize Vote counter. Adding ACCUMULATOR variable(increments by 1)
total_votes = 0
# 1.1 Candidate Options annding an empty list to be filled
candidate_options = []
# 1.2 Declare Empty Dictionary to house the candidates and their votes
candidate_votes = {}
# 1.3 Winning Candidate and winning count tracker
winning_candidate = ""  #set winning candidate string = null
winning_count = 0       #set winning count var = 0
winning_percentage = 0  #set winning pct var = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:
        # see: 1.0 Increment and add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # see: 1.1 Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # see: 1.2 Begin Tracking candidates vote count.  dict[key]
            candidate_votes[candidate_name] = 0

        # see: 1.2 Increment and add to candidate vote count. Aligned with the 'FOR' loop
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)




