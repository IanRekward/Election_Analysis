#*************************************************************************
#If Statements
counties = ["Arapahoe", "Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

#if-else statements
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#nested if-else statements
score = int(input("WHAT IS YOUR TEST SCORE? "))

if score >= 90:
    print('your grade is an A.')
else:
    if score >= 80:
        print('your grade is a B.')
    else:
        if score >= 70:
            print('your grade is a C.')
        else:
            if score >= 60:
                print('your grade is a D.')
            else:
                print('your grade is an F.')   

# Same usecase, but using if elif else statements foe ease of reading

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')           

#********************************************************************
# Membership Operators
# 'in' and 'not in'

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is NOT in the list of counties")    

# Logical Operators ******************
# 'and' 'or' 'not'
counties = ["Arapahoe", "Denver", "Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso is NOT in the list of counties")    

#**********************************************************************
#LOOPS condition-controlled and count-controlled

