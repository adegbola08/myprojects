 # This program takes any word and prints out the same word with all the vowels removed ( a, e, i, o, and u.)
# and also it capitalizes all the consonants.
# For instance, if the user types universe, the program outputs NVRS.
# This program continues running till the user wants to quit.
# Inputs = The user enters a word
# Outputs = The program removes all the vowels (a, e, i, o, u) and prints out only the consonants in the word
# entered

def main():
    start_prog()  # This function call starts the program as the user runs it.

def start_prog():
    word_input = input("Enter a word: ")  # Takes a string input from the user
    word = word_input.lower()  # Makes sure the string is converted to lowercase so it can pick out all the vowels
    vowel = ["a", "e", "i", "o", "u"]  # Defining the English vowels in a list
    space = "\n"  # This is to make a space between the printed output and before the program restart
    for i in word:  # For each character in the user input (the word entered by the user)
        if i in vowel:  # If the character is present in the defined vowel
            continue   # Skip over the character in word that is present in vowels
        print(i.upper(), end='')  # Print the remaining words in uppercase and on the same line
    print(space)  # Prints a space before continuing the program
    end_prog()   # Calls the function that gives the user a choice to end the program

def end_prog():
    while True:
        try:  # This does not make python freak out even when the user enters a non integer input
            x = int(input("Do you want to continue using this program? \n1 = YES \n0 = NO \nENTER YOUR CHOICE: "))
            if x == 1:
                start_prog()  # If user chooses to continue then call on this function to restart the program
            elif x == 0:
                print("Goodbye!")
                break  # If user enters 0 then end the program
            else:
                print("You Entered An Unassigned Number")  # For the user to enter a correct choice
                end_prog()
            break

        except:
            print("Please enter an integer!!")  # This message prints to the screen when the user
            # enters a non-integer


# Running code
main()
