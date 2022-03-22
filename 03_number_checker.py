#function goes here

def int_check(question, low_num, high_num):
    error = "Please enter a whole number between {}" \
            "and {}".format(low_num, high_num)
    valid = False
    while not valid:

        try:
            response = int(input(question))
            return response
        except ValueError:
            print(error)

#main routine goes here
