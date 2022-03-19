""" This program assigns seats on an airplane. The airplane has 10 seats.
The program asks if the passenger requires a vegetarian meal or a standard meal.
There are only 5 vegetarian meals available.
The seats are numbered 1-10 and no double seat can be assigned.
If a passenger requires a vegetarian meal but it is not available , the system gives a choice of standard meal
or printout "Next flight with a vegetarian option leaves in 4 hours".
Input: The user enters names for each passenger and also selects options provided as assigned to each numbers
Output: The program prints the First Name , Last Name, seat number, and a V for Vegetarian or S for standard meal.
If all the seats are taken, the program tells the user so and that "Next flight leaves in 4 hours"."""

lst = []


def main():
    meal_choice()
    out()
    exit_program()


def airline_intro():
    print("Hello! Welcome to TellyTubby Airlines. We are a new startup and our max capacity is 10. "
          "We offer two choices of meals")


def meal_choice():
    noOfVegMeal = 0
    i = 0
    while i < 10:
        airline_intro()
        y = i + 1  # to assign seat number
        try:
            a = int(input("We have the following meal choice. \n1 - Standard Meal\n2 - Vegetarian Meal"
                          "\nEnter an assigned number to select your choice: "))

            if a == 1:
                b = input("Please Enter Your First Name: ").title().lstrip()
                c = input("Please Enter Your Last Name: ").title().lstrip()
                print("FULL-NAME:", b, c, "\tYOUR SEAT NUMBER:", y,
                      "\tMEAL CHOICE: S-meal\n")
                s_app = "FULL-NAME: {0} {1} \tSEAT NUMBER: {2} \tMEAL CHOICE: S-meal\n"
                lst.append(s_app.format(b, c, y))

            elif a == 2:
                if noOfVegMeal < 5:
                    noOfVegMeal += 1
                    d = input("Please Enter Your First Name: ").lstrip().title()
                    e = input("Please Enter Your Last Name: ").title().lstrip()
                    print("FULL-NAME:", d, e, "\tYOUR SEAT NUMBER:", y,
                          "\tMEAL CHOICE: V-meal\n")
                    s_app = "FULL-NAME: {0} {1} \tSEAT NUMBER: {2} \tMEAL CHOICE: V-meal\n"
                    lst.append(s_app.format(d, e, y))

                else:
                    try:
                        print("\nSORRY, WE ARE OUT OF VEGETARIAN OPTIONS. CONSIDER THE FOLLOWING OPTIONS")
                        change_opt = int(input("1. Change to a Standard Meal\n2. No, I am strictly a Vegetarian"
                                               "\nEnter Your Choice: "))
                        if change_opt == 1:
                            i -= 1
                        elif change_opt == 2:
                            i -= 1
                            print("SORRY, WE ARE OUT OF VEGETARIAN OPTIONS. NEXT FLIGHT IN 4 HOURS\n")
                        else:
                            i -= 1
                    except:
                        i -= 1

            else:
                i -= 1
        except:
            print("Please Enter an Integer\n")
            i -= 1
        i += 1

    print("SORRY, WE ARE OUT OF SEATS. NEXT FLIGHT LEAVES IN 4 HOURS. PLEASE BEAR WITH US\n")


def out():
    print("\nTHIS IS TELLYTUBBY AIRLINES' ROSTER FOR NEXT FLIGHT ABOUT TO TAKE-OFF")
    for i in range(10):
        print(str(i+1)+".  "+lst[i])


def exit_program():
    try:
        a = int(input("Enter Any Number To Use This Program Again | 0 to Exit\nEnter Your Choice: "))
        if a == 0:
            print("Goodbye!!!")
        else:
            main()

    except:
        print("Please Enter an Integer!")
        exit_program()


# Running Code
main()
