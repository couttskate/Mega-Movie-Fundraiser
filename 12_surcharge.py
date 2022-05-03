import ...

# Function goes here
# WARNING: The response is returned in Title Case
# checking that input is either 'yes' or 'no'
def string_check(choice, options):

    is_valid = ""
    chosen = ""

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
