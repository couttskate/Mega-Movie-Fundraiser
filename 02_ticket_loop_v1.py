#start of loop

#initialise loop so that it runs at least once

name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    #get details
    name = input("Name: ")
    count += 1
    print("You have {} seats left".format(MAX_TICKETS - count))
if count < MAX_TICKETS:
    print("You have sold {} tickets.There are {} places still avaliable.".format(count, MAX_TICKETS - count))

else:
    print("You have sold all avaliable tickets.")
