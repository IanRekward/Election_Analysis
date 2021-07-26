# The data we need to retrieve
# 1-The total bumber of votes cast
# 2-A complete list of all candidates who received votes
# 3-The percentage of votes each candidate received ot total votes
# 4-The total number of votes each candidate received
# 5-The winner of the election based on popular vote

# The data we need to retrieve
import csv  #dir(csv) to view all functions in csv module
# import random
# import numpy 

# file_variable = open(filename, mode)
# filename is a string specifying the name of the file

# mode
# "r": Open a file to be read.
# "w": Open a file to write to it. This will overwrite an existing file and create a file if one does not already exist.
# "x": Open a file for exclusive creation. If the file does not exist, it will not create one.
# "a": Open a file to append data to an existing file. If a file does not exist, it creates one, if a file has been created the data will be added to the file.
# "+": Open a file for reading and writing.

#*************************************************************************
#Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

#Read data from a file
#assign a variable for the file to load and the path.
file_to_load = 'Resources\election_results.csv'

election_data = open(file_to_load, 'r')
#To do: perform analysis

#Close the file.
election_data.close()

#*************************************************************************
#The with statement opens the file and ensures proper acquisition or release 
# of any data without having to close the file, to ensure that the data isn't lost or corrupted.
# with open(filename) as file_variable

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

import os 
# Chaining multiple method calls:  os.path.join("Resources", "election_results.csv")

#*************************************************************************
#Read data from a csv
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

#*************************************************************************
# Write data to a csv

# Create a filename variable to a direct or indirect path to the file.
# creating an empty txt file in the desired folder
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w") 

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")
# Close the file
outfile.close()

# Same as above, but cleaner ***********

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # txt_file.write("Hello World!!")
    # Write three counties to the file.
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")
# OR 
    # Write three counties to the file.
    txt_file.write("Arapahoe, Denver, Jefferson")

# to write the counties on seperate lines us \n as the 'new line' operator
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:

    txt_file.write("Counties in the Election")
    txt_file.write("\n-------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")


#*************************************************************************
#
#*************************************************************************
#
