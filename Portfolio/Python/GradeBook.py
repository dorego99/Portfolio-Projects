print("Grade Book")
menu = """
0: Exit.
1: Display a sorted list of grades.
2: Add a grade to the list.
"""

gradeList = []

done = False

while not done:
    print(menu)
    selection = input("please make a selection: ")
    print()
    if selection == "0":
        done = True
    elif selection == "1":
        if(len(gradeList) == 0):
            print("Grade Book empty")
        else:
            print("Grade Book")
            print("-"*16)
            for grade in gradeList:
                print(grade)
    elif selection == "2":
        x = input("Add a grade: ")
        grade = x.title()
        gradeList.append(grade)
    else:
        print("not a valid entry!")
        print()