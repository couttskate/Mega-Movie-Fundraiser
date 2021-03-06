# import statements
import pandas
import re

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
        if MAX_TICKETS - ticket_count == 1:
            # warns user there is only 1 seat left
            print("There is ONE place still avaliable.")
        else:
            print("There are {} places still avaliable.".format(MAX_TICKETS - ticket_count))

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

# checking that input is either 'yes' or 'no'
def string_check(choice, options):

    for var_list in options:

        #if the snack is in one of the lists, return the full
        if choice in var_list:

            #get full name of the snack and put it
            #in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen snack is not valid, set snack_ok to no
        else:
            is_valid = "no"

    #if the snack is not ok - ask question again
    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"

# gets list of snacks
def get_snack():
    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # each item in valid snacks is a list with
    # valid options for each snack <full name, letter code (a-e)
    # , and possible abbreviations etc>
    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&M's", "m&m's", "mms", "m", "b"], # first item is M&M's
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "d"],
        ["orange juice", "oj", "o", "j", "juice", "e"]
    ]

    # holds snack order for a single user.
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        # if item has a number, separate it into two (number / item)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        # check snack amount is valid (less than 5)
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

        # add snack AND amount to list...
        snack_row.append(amount)
        snack_row.append(snack_choice)

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)
# _________Main Routine_________

# set up dictionaries/lists needed to store data

# list for valid yes/no responses
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]
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

    # asks user if they want a snack
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_check(want_snack, yes_no)

    # if they say yes, ask what snacks they want (and add to our snack
    if check_snack == "Yes":
        get_order = get_snack()

    else:
        get_order = []

    # show snack orders
    print()
    if len(get_order) == 0:
        print("Snacks Ordered: None")

    else:
        print("Snacks Ordered:")

        """for item in snack_order:
            print(item)"""

        print(get_order)
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
