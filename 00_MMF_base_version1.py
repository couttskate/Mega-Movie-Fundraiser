#kate coutts
#15march2022
#Mega Movie Fundraiser


#import statements

#functions go here

#checks that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)
        #if name is not blank, program continues
        if response != "":
            return response
        #if name is blank, show error (and repeat loop)
        else:
            print("Sorry - this can't be blank, "
                  " please enter your name")


#''''''''Main Routine '''''''

#Set up dictionaries/lists needed to hold data

#Ask user if they have used the program before and show instructions if necessary

#Loop to get ticket details
#start of loop

#initialise loop so that it runs at least once

name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    #get details

    #Get name (can't be blank)
    name = not_blank("Name: ")
    count += 1
    if MAX_TICKETS - count != 1:
        print("You have {} seats left".format(MAX_TICKETS - count))
    else:
        # warns user that there is ONE seat left
        print("You have ONE seat left.")

if count < MAX_TICKETS:
    print("You have sold {} tickets. \n There are {} places still avaliable.".format(count, MAX_TICKETS - count))

else:
    print("You have sold all avaliable tickets.")

    #Get age (between 12 and 130)

    #Calculate ticket price

    #Loop to ask for snacks

    #Calculate snack price

    #Loop to ask for snacks

    #Calculate snack price

#Ask for payment method (and apply surcharge if necessary)

#Calculate total sales and profit

#Output data to text file
