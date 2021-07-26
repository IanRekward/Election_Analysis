#print("Hello World!")
# type(3)
# type(2019)

# type(True)
# Help("Keywords")

counties = ["Arapahoe", "Denver", "Jefferson"]
counties[0]
print(counties[-1])
len(counties)

# slicing ato get at pieces of a list
# list[start : end] 

counties[0 : 2] #will display first and last items in the list
counties[0:1]   #will display the first iteam in the list
counties[:2]    #will return everything up to position 2

# add items to a list using .append()
counties.append("El Paso") #adds El Paso to the end of the list 'counties'

#list.insert(index, obj) to add a item to the list in a specific place
counties.insert(2, "El Paso") #adds El Paso into the second position in the list

#.remove() to remove an item from a list
counties.remove("El Paso") #removes the first instance of El Paso from the list, but keeps subsiquent instances

# pop() to remove an item from an index position in a list
counties.pop(2) #removes the instance of El Paso from the counties list based on its index position

# change elements in a list
counties[2] = "El Paso" #Replaces 'Jefferson' with 'El Paso' in the list
counties

#Tuples: similar to a list, but it is immutable and cannot be changed like a list can
# my_tuple = ( ) #or
# my_tuple = tuple()

counties_tuple = ("Arapahoe", "Denver", "Jefferson")
#****************************************************************************************************************************
#Dictionaries

#{key:value} uses {} Curly braces

#to create or initialize an empty dictionary
#my_dictionary = {} #or
#mydictionary = dict{}

counties_dict = {} #creates an empty dictionary
counties_dict["Arapaho"] = 422829 #adds Arapaho as the Key and 422829 as the Value
counties_dict #displays as {'Arapaho:42829}
#add denver and jefferson to the dictionary
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

# Display all keys AND values in a dictionary
print(counties_dict) #or
counties_dict.items()

counties_dict.keys() #Display all 'keys' in a dictionary
counties_dict.values() #Display all 'values' in a dictionary
counties_dict.get("Denver") # retrieve a specific 'value' from a dictionary
counties_dict["Arapaho"] # printing a 'key' will return the value of that specific key

# Lists of Dictionaries
# each entry is itself, a dictionary. 
voting_data = [] #creating an empy list
voting_data.append({"county":"Arapaho", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Jefferson", "registered_voters":432438})
voting_data.insert(2,({"county":"El Paso", "registered_voters":461149}))
# voting_data.pop(3)
voting_data
#**********************************************************************************

#Decision Statements

#declare votes as a user-entry field with a type of int
my_votes = int(input("How many votes did you get in the election?  "))
total_votes = int(input("What is the total number of votes in the election?  "))
pct_votes = (my_votes/total_votes)*100
print("I received " + str(pct_votes)+ "% of the total votes.")












