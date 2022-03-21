#start of loop

#initialise loop so that it runs at least once

name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    #get details
    name = input("Name: ")
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
