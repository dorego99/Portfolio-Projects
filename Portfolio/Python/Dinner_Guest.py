"""
Charles Valenca
SEC 290
Programming Assignment 4
Febuary 6 2021
"""

#prints guest list manager and creates menu variable
print("Guest List Manager")
print("-"*16)
menu = """
0: Exit.
1: Display a sorted list of guests.
2: Add a guest to the list.
3: Delete a guest from the list.
"""
#displays where the variable guestList will be displayed

guestList = []


#creates done variable
done = False

#creates while not condition to print menu and ask user for selection
while not done:
    print(menu)
    selection = input("please make a selection: ")
    print()
#creates if statement to end program when 0 is selected
    if selection == "0":
        done = True
#creates elif statement for the first to print guest statement and identifies if the guest list is empty and notifies the user
    elif selection == "1":
        if(len(guestList) == 0):
            print("Guest list empty")
        else:
            print("Guest List")
            print("-"*16)
            for guest in guestList:
                print(guest)
#creates elif statement for the second selection to add a guest to the list and capitalize the first letter while lowercasing the rest
    elif selection == "2":
        x = input("Add a guest: ")
        guest = x.title()
        guestList.append(guest)
#creates elif statement for the third selection to remove a guest from a list and capitalize the first letter while lowercasing the rest
    elif selection == "3":
        x = input("Remove a guest: ")
        guest = x.title()
#creates if else statement to identify if a guest is in the list
        if guest in guestList:
            guestList.remove(guest)
        else:
            print("Guest name not found")
#creates else statement incase user chooses and entry that is not valid
    else:
        print("not a valid entry!")
        print()