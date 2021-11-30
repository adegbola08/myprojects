""" This program rolls two dices 100 times and shows the results as the sum of the two dices.
Each toss is random like in real life.
The dice used is a standard dice with values from 1 to 6.
Input = The program takes input of the user's choice to continue running or exit the program
Output = The program displays the sum of the two rolls and also displays the most frequently generated sum of the 100
"""

import random    # imports a library that helps pick random numbers

lst1 = []  # creates an empty list that helps save the results of the first tosses
lst2 = []  # creates an empty list that helps save the results of the second tosses
lst = []   # the list that saves the sum of the first and second tosses

def main():
    coin_toss1()
    coin_toss2()  # calls the function
    add_list()  # calls the function
    most_shown()  # calls the function
    end_program()  # calls the function


def coin_toss1():
    lst1.clear()  # ensures the list is cleared in case the program is re-running
    for i in range(100):   # for each number in the range of 100 (i.e from 0-99)
        lst1.append(random.randint(1, 6))  # append method is same as the update method in set and dict data types
        i += 1  # increments the value of i in the for loop


def coin_toss2():
    lst2.clear()  # ensures the list is cleared in case the program is re-running
    for i in range(100):
        lst2.append(random.randint(1, 6))  # append method is same as the update method in set and dict data types
        i += 1  # increments the value of i in the for loop


def add_list():
    lst.clear()  # ensures the list is cleared in case the program is re-running
    for i in range(len(lst1)):
        lst.append(lst1[i] + lst2[i])
        i += 1  # increments the value of i in the for loop
    for i in lst:
        print(i)


def most_shown():
    jk = list(set(lst))
    # print(jk) # test printing the new list
    new = []  # new list to store my count result
    for i in jk:
        b = lst.count(i)
        new.append(b)
    # print(new)  # to show that the count is correct
    f = new.index(max(new))
    # print(f)  # to show that it picks the max number's correct index
    y = jk[f]
    print("The most frequently appeared sum is", y)


def end_program():
    try:  # keeps the program running until user enters an integer
        k = int(input("Enter Any Number To Continue | 0 to Exit\n"))
        if k == 0:
            print("Goodbye")
        else:
            main()

    except:  # keeps the program running until user enters an integer
        print("Please enter an integer")
        end_program()


# Running code
main()