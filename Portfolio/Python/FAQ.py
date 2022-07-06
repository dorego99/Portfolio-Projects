"""
Charles Valenca
SEC 290
Programming Assignment 5
Febuary 13 2021
"""

#Prints the menu
print("="*16)
print("Frequently Asked Questions")
print("="*16)
menu = """
0: Exit.
1: List FAQ's
2: Add FAQ
3: Delete FAQ
"""

#adds faq list
faq = {}

#creates done variable
done = False

#asks for users input and closes program if 0 is chosen
while not done:
    print(menu)
    choice = input("please make a choice: ")
    print()
    if choice == "0":
        done = True

#if user chooses one, program displays list of items
    elif choice == "1":
        print("Frequently Asked Questions")
        print("="*16)
        for question,answer in faq.items():
            print("Question: {}".format(question))
            print("Answer: {}".format(answer))
            print()

#if 2 is chosen program asks user to input a question
    elif choice == "2":
        question = input("Add a question: ")
        
#if user inputs a new question, the program notifies them and asks them to refrase
        while question in faq:
            print("This question has already been added!")
            question = input("Please refrase the question: ")
#asks user to add an answer
        else:
            answer = input("Add an answer: ")
            faq[question] = answer
            print()
            print("Question Added!")

#deletes any question the user inputs to delete and lets the user know if the question was not found
    elif choice == "3":
        question = input("Delete question: ")
        if question in faq:
            faq.pop(question)
            print()
            print("Question deleted")
        else:
            print()
            print("Question not found!")

#notifies the user if they chose an invalid entry
    else:
        print("not a valid entry!")
        print()
        