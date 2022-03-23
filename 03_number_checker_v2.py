#function goes here

#checks for an integer more than 0
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

#main routine goes here

age= int_check("Age: ", 12, 130)
