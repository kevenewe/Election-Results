#import data
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

#print the header row.
    headers = next(file_reader)
    print(headers)
#print each row in the csv file
    #for row in file_reader:
     #   print(row)

# Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, "w") as txt_file:


    # Write some data to the file.
    # txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")
#Read the file object with the reader function.


#to do: perform analysis

#close the file.


#total number of votes cast

# list of candidate who received votes

# total number of votes each candidate won

# percentage of votes each candidate wond

# Winner of the election based on pupular vote. 