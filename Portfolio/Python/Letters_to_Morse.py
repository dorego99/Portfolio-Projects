"""
Charles Valenca
SEC 290
Programming Assignment 3
January 30, 2021
"""

#creates text_to_morse function. creates if elif else statements which is indented for the function. Creates return function.
def text_to_morse(letter):
    if letter == "A":
        morse_code = ".-"
    elif letter == "B":
        morse_code = "-..."
    elif letter == "C":
        morse_code = "-.-."
    elif letter == "D":
        morse_code = "-.."
    elif letter == "E":
        morse_code = "."
    elif letter == "F":
        morse_code = "..-."
    elif letter == "G":
        morse_code = "--."
    elif letter == "H":
        morse_code = "...."
    elif letter == "I":
        morse_code = ".."
    elif letter == "J":
        morse_code = ".---"
    elif letter == "K":
        morse_code = "-.-"
    elif letter == "L":
        morse_code = ".-.."
    elif letter == "M":
        morse_code = "--"
    elif letter == "N":
        morse_code = "-."
    elif letter == "O":
        morse_code = "---"
    elif letter == "P":
        morse_code = ".--."
    elif letter == "Q":
        morse_code = "--.-"
    elif letter == "R":
        morse_code = ".-."
    elif letter == "S":
        morse_code = "..."
    elif letter == "T":
        morse_code = "-"
    elif letter == "U":
        morse_code = "..-"
    elif letter == "V":
        morse_code = "...-"
    elif letter == "W":
        morse_code = ".--"
    elif letter == "X":
        morse_code = "-..-"
    elif letter == "Y":
        morse_code = "-.--"
    elif letter == "Z":
        morse_code = "--.."
    else:
        morse_code = "Unknown"
    return(morse_code)

#creates a loop/ asks the user to input their letter 4 times. converts the text_to_morse function into a variable and prints that variable.
for letter in range(4):
    letter = input("Please enter an uppercase letter: ")
    morse = text_to_morse(letter)
    print(morse)
