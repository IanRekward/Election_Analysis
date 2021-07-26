#*******************************************************************
# While Loops: are 'condition' contolled 
    # set x(the loop var alias to 0 and then set the condition under 
    # which it will operat and cease)
x = 0
while x <= 5:
    print(x)
    x = x + 1

#*******************************************************************
# For Loops: are 'count' conrolled amd iterate a specifict number of 
# times before terminating
    #county is declared as a variable and set equal to the first item
    #in the list of counties, "Arapahoe". on the second iteration 
    #county is set equal to the next item in the list "Denver" and so on
counties = ["Arapahoe", "Denver","Jefferson"]    
for county in counties:
    print(county)    

numbers = [1,2,3,4]
for num in numbers:
    print(num)

# Range Function
for num in range(5):
    print(num)

# using Indexing to iterate
for i in range(len(counties)):
    print(counties[i])

#iterating through a Dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}    

for county in counties_dict:
    print(county)
#alternatively we can use the 'keys' method for iterating through a dictionary
for county in counties_dict.keys():
    print(county)

#iterates through the keys to and returns the values of the keys
for county in counties_dict:
    print(counties_dict[county])

#Return Key and Value pairs from a dictionary. **feels complicated
for key, value in counties_dict.items(): #referencing 'key' and 'value'
    print(key,value) 

#same as above, but referencing 'key' and 'value' using the names of the keys and value
for county, voters in counties_dict.items(): 
    print(county, voters)                         

#*******************************************************************
#Iterating through a List of Dictionaries
counties_dict = {}
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "registered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data: #basic 'for' loop
    print(county_dict)

for i in range(len(voting_data)): #'for loop with range function
    print(voting_data[i])

#returns each
# {'county': 'Arapahoe', 'registered_voters': 422829}
# {'county': 'Denver', 'registered_voters': 463353}
# {'county': 'Jefferson', 'registered_voters': 432438}


#*******************************************************************
# Get Values(only) from a LIST of Dictionaries using the .values(): method
for county_dict in voting_data:
    for value in county_dict.counties_dict.values():
        print(value)
#returns each VALUE from each KEY
# Arapahoe
# 422829
# Denver
# 463353
# Jefferson
# 432438

#*******************************************************************
# iterates through all DICTIONARIES and prints county name only
for county_dict in voting_data:
    print(county_dict['counties_dict = {}}county'])
#returns just the county names
# Arapahoe
# Denver
# Jefferson

#*******************************************************************
#*******************************************************************
#3.2.11 Printing Formats
#print("Hello World!")
#print("your interest for the year is $" + str(interest) #connicting strings with " + " 

#F-strings: Formatted String Literals
#replaces concatination?  uses curly braces to add strings {}

#origional code
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total number of votes in the elsection? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes) + "% of the total votes.")

#code using f-string
my_votes - int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total number of votes in the elsection? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Using f-strings with DICTIONARIES

#origional code
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters")

#dictionary code using f-strings
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

#Format Floating-Point Decimals
#14.466115988409808
f'{value:{width}.{precision}}'
f'{value:{width},.{precision}}' #add comma , as a thousands seperator
# :,  and :2f

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)


#*******************************************************************
# 



#*******************************************************************
# 