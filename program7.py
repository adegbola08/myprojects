"""This program translates the first 20 English numbers to another language.
The numbers should be in the form of characters not integers, so for instance 'one' and not 1.
The program can search either way, to and from English to the language of choice.
The program starts by prompting the user on how to use the translator and the language of choice and which way they want
to translate.
Input = The user types in what number (in words) they want to translate from english to french and vice versa; it also
gives the user a choice to exit
Output = The program displays the translated number"""

dic = {"one": "un", "two": "deux", "three": "trois", "four": "quatre", "five": "cinq","six": "six","seven": "sept",
        "eight": "huit", "nine": "neuf", "ten": "dix", "eleven": "onze", "twelve": "douze", "thirteen": "treize",
       "fourteen": "quartoze", "fifteen": "quinze", "sixteen": "seize", "seventeen": "dix-sept", "eighteen": "dix-huit",
       "nineteen": "dix-neuf", "twenty": "vingt"}

def main():
    lang_choice()
    end_program()

def lang_choice():
    try:
        n = int(input("HEY! THIS PROGRAM TRANSLATES NUMBERS 1- 20 (IN WORDS) FROM ENGLISH TO FRENCH AND VICE VERSA\n"
                      "1 - TRANSLATE ENGLISH TO FRENCH\n2 - TRANSLATE FRENCH TO ENGLISH\nENTER YOUR CHOICE:\n"))
        if n == 1:
            convert_eng()
        elif n == 2:
            convert_fren()
        else:
            print("Please Enter A Correct Choice")
            lang_choice()
    except:
        "Please Enter An Integer!"
        lang_choice()

def convert_eng():
    c = input("Enter the number (in English words) you wish to translate to French")
    y = c.lower()
    for i in dic:
        if y == i:
            return print(dic[y])
    print("SORRY, I CAN ONLY CONVERT THE FIRST TWENTY NUMBERS")

def convert_fren():
    b = input("Enter the number (in French words) you wish to translate to English")
    z = b.lower()
    for i in dic.values():
        if i == z:
            for y in dic:
                if dic[y] == z:
                    return print(y)
    print("SORRY, I CAN ONLY TRANSLATE THE FIRST TWENTY NUMBERS")

def end_program():
    try:  # keeps the program running until user enters an integer
        k = int(input("Enter Any Number To Continue | 0 To Exit\n"))
        if k == 0:
            print("Goodbye!!!")
        else:
            main()

    except:  # keeps the program running until user enters an integer
        print("Please enter an integer")
        end_program()


# Running Code
main()