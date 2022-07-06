print("Shopping list")
print("="*14)
menu = """
0: Exit.
1: Display the list items
2: Add an item to the list
"""

shoppingList = []

done = False

while not done:
    print(menu)
    selection = input("Please make a selection: ")
    print()
    
    if selection == "0":
        done = True
    elif selection == "1":
        if(len(shoppingList) == 0):
            print("Shopping list empty")
        else:
            print("Shopping List")
            print("-"*6)
            for item in shoppingList:
                print(item)
    elif selection =="2":
        x = input("Add an item: ")
        item = x.title()
        shoppingList.append(item)
    else:
        print("not a valid entry!")