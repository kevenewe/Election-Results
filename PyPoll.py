#import data
# Add our dependencies.
import csv
import os


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialized total_votes and sets value to 0
total_votes = 0

#Candidates
Candidate_Options =[]

Candidate_votes = {}

Vote_percentage = 0
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

#print the header row.
    headers = next(file_reader)
   # print(headers)

    for row in file_reader:
        total_votes +=1 

        candidate_name = row[2]
        if candidate_name not in Candidate_Options:
            Candidate_Options.append (candidate_name)
            Candidate_votes [candidate_name] =0
            
        Candidate_votes [candidate_name] +=1

#Save the results to text file.

with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    election_results =(
        f"\nElections Results\n"
        f"------------------------\n"
        f" total Votes: {total_votes:,}\n"
        f"------------------------\n")
    print (election_results, end="") 

    txt_file.write (election_results)

    for candidate_name in Candidate_votes:
        votes = Candidate_votes[candidate_name]    
        Vote_percentage = float (votes) / float (total_votes) * 100
        
        Candidate_results = (
            f"{candidate_name}: {Vote_percentage:.1f}% ({votes:,})\n")

        print (Candidate_results)

        txt_file.write (Candidate_results)


        if (votes > winning_count) and (Vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = Vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
            
    Winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n") 
    print (Winning_candidate_summary)
           
    

    txt_file.write(Winning_candidate_summary)

    



# Using the open() function with the "w" mode we will write data to the file.

#    print (Candidate_results)               

   # txt_file.write (election_results)
   # for candidate_name in Candidate_votes:
   #     votes = Candidate_votes[candidate_name]
   #     Vote_percentage= float (votes) / float (total_votes) * 100
       #rounded Vote_percentage
    #    rvote_percentage = round(Vote_percentage, 2)
    #    Candidate_results = (
    #        f"{candidate_name}: {rvote_percentage}% ({votes:,}\n")


    

#    txt_file.write (Candidate_results)

#Load the file object with the reader function.


#to do: perform analysis

#close the file.


#total number of votes cast

# list of candidate who received votes

# total number of votes each candidate won

# percentage of votes each candidate wond

# Winner of the election based on pupular vote. 