# import statements
import re
import pandas

# functions go here

# checks that ticket name is not blank
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

# checks that numbers are valid
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

# checks number of tickets left and warns user
# if maximum is being approached
def check_tickets(ticket_count, MAX_TICKETS):
    # tell user if they have unsold tickets
    if ticket_count < MAX_TICKETS:
        print("You have sold {} tickets.".format(ticket_count))
        if ticket_count != 1:
            print("There are {} places still avaliable.".format(MAX_TICKETS - ticket_count))

        # warns user there is only 1 seat left
        else:
            print("There is ONE place still avaliable.")

    else:
        print("You have sold all avaliable tickets.")

    return ""

# gets ticket price based on age
def get_ticket_price():
    # Get age (between 12 and 130)
    age= int_check("Age: ")

    # check that age is valid
    if age < 12:
        print("Sorry you are too young for this movie.")
        return "invalid ticket price"

    elif age > 130:
        print("That is very old - it looks like a mistake.")
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.50
    elif age > 64:
        ticket_price = 6.50
    else:
        ticket_price = 10.50

    return ticket_price

# _________Main Routine_________

# set up dictionaries/lists needed to store data

# initialise loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# initialise lists (to make data frame in due course)
all_names = []
all_tickets = []

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

# Ask user if they have used the program before and show instructions if necessary

# Loop to get ticket details

while name != "xxx" and ticket_count < MAX_TICKETS:

    # check numbers of ticket limit has not been exceeded
    check_tickets(ticket_count, MAX_TICKETS)

    # Get details for each ticket

    # Get name (can't be blank)
    name = not_blank("Name: ")

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    # Get ticket price based on age
    ticket_price = get_ticket_price()
    # if the age is invalid, restart loop (and get name again)
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

   # get snacks
   # get payment method

# end of tickets/snacks/payment loop

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

# calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# tell user if they have unsold tickets
if ticket_count < MAX_TICKETS:
    print("You have sold {} tickets.".format(ticket_count))
    if ticket_count == 1:
        print("There are {} places still avaliable.".format(MAX_TICKETS - ticket_count))
    else:
        print("There is one place still avaliable.")

else:
    print("You have sold all avaliable tickets.")


    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Loop to ask for snacks

    # Calculate snack price

# Ask for payment method (and apply surcharge if necessary)

# Calculate total sales and profit

# Output data to text file
