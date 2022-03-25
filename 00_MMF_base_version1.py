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

#checks that numbers are valid
def int_check(question):
    error = "Please enter a whole number that is more than 0"
    valid = False
    while not valid:

        # ask user for number and check if it is valid
        try:
            response = int(input(question))

            if  response <= 0:
                print(error)
            else:
                return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)

#''''''''Main Routine '''''''

#Set up dictionaries/lists needed to hold data

#Ask user if they have used the program before and show instructions if necessary

#Loop to get ticket details
#start of loop

#initialise loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

while name != "xxx" and ticket_count < MAX_TICKETS:

    #get details

    #Get name (can't be blank)
    name = not_blank("Name: ")
    #end the loop if the exit code is entered
    if name == "xxx":
        break

    #Get age (between 12 and 130)
    age= int_check("Age: ")

    #check that age is valid
    if age < 12:
        print("Sorry you are too young for this movie.")
        continue

    elif age > 130:
        print("That is very old - it looks like a mistake.")
        continue

    if age < 16:
        ticket_price = 7.50
    elif age > 64:
        ticket_price = 6.50
    else:
        ticket_price = 10.50


    ticket_count += 1
    ticket_sales += ticket_price

    print("{} : ${:.2f}".format(name, ticket_price))

    if MAX_TICKETS - ticket_count != 1:
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))
    else:
        # warns user that there is ONE seat left
        print("You have ONE seat left.")
#end of tickets loop

#calculate profit etc
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

#tell user if they have unsold tickets
if ticket_count < MAX_TICKETS:
    print("You have sold {} tickets.".format(ticket_count))
    if ticket_count > 1:
        print("There are {} places still avaliable.".format(MAX_TICKETS - ticket_count))
    else:
        print("There is one place still avaliable.")

else:
    print("You have sold all avaliable tickets.")


    #Calculate ticket price

    #Loop to ask for snacks

    #Calculate snack price

    #Loop to ask for snacks

    #Calculate snack price

#Ask for payment method (and apply surcharge if necessary)

#Calculate total sales and profit

#Output data to text file
