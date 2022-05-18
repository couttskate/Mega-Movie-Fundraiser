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
        ["popcorn", "p", "pop", "corn", "a"],
        ["M&Ms", "M&Ms", "mms", "mm" "m", "b"], # first item is M&Ms
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "h20", "d"],
        ["orange juice", "oj", "o", "j", "juice", "e"]
    ]

    # holds snack order for a single user.
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx" or desired_snack != "n":

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

# list of valid responses for payment method
pay_method = [
    ["cash", "ca"],
    ["credit","cr"]
]


# initialise loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# initialise lists (to make data frame in due course)
all_names = []
all_tickets = []

# Snack lists
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Store surcharge multiplier
surcharge_mult_list = []

# Lists to store summary data...
summary_headings = ["Popcorn", "M&M's", "Pita Chips", "Water",
                    "Orange Juice", "Snack Profit", "Ticket Profit",
                    "Total Profit"]
summary_data = []

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_mult_list

}

# Summary Dictionary
summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

# Cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
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
    snack_order = get_snack()


    # Assume no snacks have been bought...
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    # ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash / credit)").lower()
        how_pay = string_check(how_pay, pay_method)

    # apply surcharge (if necessary)
    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

    surcharge_mult_list.append(surcharge_multiplier)

# end of tickets/snacks/payment loop

# print details
# Create dataframe and set index to name column
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called 'Sub Total'
# fill it with price for snacks and ticket

movie_frame["Snacks"] = \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice']

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Snacks']

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']

# Shorten column names
movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                            'Pita Chips':'Chips',
                                            'Surcharge_Multiplier':'SM'})

# Set up summary dataframe
# populate snack items...
for item in snack_lists:
    # sum items in each snack list
    summary_data.append(sum(item))

# Get snack profit
# Get snack total from panda
snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2
summary_data.append(snack_profit)

# Get ticket profit and add to list
ticket_profit = ticket_sales - (5 * ticket_count)
summary_data.append(ticket_profit)

# Work out total profit and add to list
total_profit = snack_profit + ticket_profit
summary_data.append(total_profit)

# Create summary frame
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index('Item')

# Set up columns to be printed ...
pandas.set_option('display.max_columns', None)

# Display numbers to 2 dp...
pandas.set_option('display.precision', 2)

print()
print("*** Ticket / Snack Information ***")
print("Note: for full details, please see the excel file called")
print()
print(movie_frame[['Ticket', 'Snacks', 'Sub Total',
                   'Surcharge', 'Total']])

print()

print("*** Snack / Profit Summary ***")
print()
print(summary_frame)

# Tell user if they have unsold tickets
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
