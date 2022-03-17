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
        if response != "":
            return response
        else:
            print("Sorry - this can't be blank, "
                  " please enter your name")


#''''''''Main Routine '''''''

#Set up dictionaries/lists needed to hold data

#Ask user if they have used the program before and show instructions if necessary

#Loop to get ticket details

    #Get name (can't be blank)

    #Get age (between 12 and 130)

    #Calculate ticket price

    #Loop to ask for snacks

    #Calculate snack price

    #Loop to ask for snacks

    #Calculate snack price

#Ask for payment method (and apply surcharge if necessary)

#Calculate total sales and profit

#Output data to text file
