"""
This is my final project program for my python class
This is a program that takes in strings and evaluates them. This program is capable of performing multiple tasks.
Firstly, it could be used to check if two words are anagrams. (Anagram: a word is an anagram of another if when
rearranged can be used to form the other word). E.g., crate and trace are anagrams.
Secondly, it would be able to identify palindromes. (Palindrome: a word is a palindrome if when reversed
would give the same word as when in place). E.g., Bob is a palindrome
And lastly, the program would be capable of checking for the longest common prefix among a list of words.
E.g., if the user inputs [flower, flow, flight], the program return "fl".
Inputs = The user enters his/her choice of operation using assigned numbers; the user also provides strings for
evaluation based on what operation the user is performing
Outputs = The program displays the evaluation results for every operation performed on the strings inputted by the
user
"""


def main():
    print("THIS A VERY COOL PROGRAM THAT CAN TELL ANAGRAMS, CHECK PALINDROME, AND CHECK THE LONGEST COMMON PREFIX")
    choice()


def choice():
    try:
        user = int(input("What operation would you like to perform?\n1 - Check if two words are anagrams of each other"
                         "\n2 - Check if a word is palindromic\n3 - Check the longest common prefix in a list"
                         "\n0 - To Exit\nEnter your choice: "))
        if user == 1:
            word1 = input("Enter the first word: ")
            word2 = input("Enter the second word: ")
            anagram(word1, word2)
            print("\n")
            choice()

        elif user == 2:
            word = input("Enter the word you want to check if it's a palindrome: ")
            palindrome(word)
            print("\n")
            choice()

        elif user == 3:
            no_of_words = int(input("How many words do you want to put in the list? "))
            lst = []
            for i in range(no_of_words):
                word = input("Enter word: ")
                lst.append(word)
            longest_common_prefix(lst)
            print("\n")
            choice()

        elif user == 0:
            end_program()

        else:
            print("That is not assigned\n")
            choice()

    except:
        print("That is not a correct input!\n")
        choice()


def anagram(word1, word2):
    word_1 = word1
    word_2 = word2
    word1 = list(word1)
    word2 = list(word2)
    if len(word1) != len(word2):
        return print("OOPS, %s IS NOT AN ANAGRAM OF %s" % (word_1.upper(), word_2.upper()))

    for i in range(len(word1)):
        if word1[i] in word2:
            word2.remove(word1[i])
            i += 1
        else:
            return print("OOPS, %s IS NOT AN ANAGRAM OF %s" % (word_1.upper(), word_2.upper()))
    return print("YES, %s IS AN ANAGRAM OF %s" % (word_1.upper(), word_2.upper()))


def palindrome(word):
    c = ""
    for i in word:
        if i.isalnum():
            c += i
        else:
            continue
    y = ("".join(reversed(c)))
    if y.lower() == c.lower():
        return print("YES, %s IS A PALINDROME!" % word.upper())

    else:
        return print("OOPS, %s IS NOT A PALINDROME" % word.upper())


def longest_common_prefix(lst):
    shortest = min(lst, key=len)
    res = ""
    for i in range(len(shortest)):
        for j in range(len(lst)):
            p = lst[j]
            if shortest[i] == p[i]:
                j += 1
            else:
                if not res:
                    return print("THERE IS NO COMMON PREFIX")
                else:
                    return print("THE LONGEST COMMON PREFIX IS", res)
        res += shortest[i]
        i += 1
    return print("THE LONGEST COMMON PREFIX IS", res)


def end_program():
    try:  # keeps the program running until user enters an integer
        k = int(input("\nAre you sure you want to Exit?\n1 - Continue using program\n0 - EXIT\nEnter your choice: "))
        if k == 0:
            print("Goodbye!!!")
        elif k == 1:
            print("\n")
            main()
        else:
            print("That's not assigned")
            end_program()

    except:  # keeps the program running until user enters an integer
        print("Please enter an integer")
        end_program()


main()
