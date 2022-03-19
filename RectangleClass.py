""" This program contains a class called Rectangle. The class uses a constructor (initializing method)
that takes its two sides.  Each time a new rectangle is instantiated, the class assigns a unique number
to it, it calculates its area and perimeter and stores all the data in an instance of its class.
The program asks the user to create a new rectangle or to display an already stored rectangle.
Each time a rectangle is asked to be displayed, all its info should be displayed: its unique number,
its sides, its area, and its perimeter. The user decides when to quit the program.
The program should self-guard itself against invalid inputs such as strings or negative numbers.
Inputs = user enters length, breadth of the triangle. User decides to continue or quit
Output = the program displays created rectangles' details
"""


lst = []
lst2 = []


class Rectangle:
    Counter = 2100

    def __init__(self, length, breadth):
        Rectangle.Counter += 15
        self.length = length
        self.breadth = breadth
        self.area = (self.length * self.breadth)
        self.perimeter = 2*(self.length + self.breadth)
        self.unique_no = Rectangle.Counter
        lst.append(self.unique_no)

    def rectangle_info(self):
        a = "Length: {0} Breadth: {1} Area: {2} Perimeter: {3} Unique No: {4}"
        print_a = (a.format(self.length, self.breadth, self.area, self.perimeter, self.unique_no))
        lst2.append(print_a)
        return print_a

    def __repr__(self):
        return self.rectangle_info()


def choice():
    try:
        print("THIS PROGRAM COULD BE USED TO CREATE AND DISPLAY CREATED RECTANGLES")
        y = int(input("1 - To create a new rectangle\n2 - To display a stored rectangle\nEnter your choice: "))
        if y == 1:
            try:
                leng = int(input("Enter the length of the Rectangle: "))
                bred = int(input("Enter the breadth of the Rectangle: "))
                par = Rectangle(leng, bred)
                print(par.rectangle_info(), "\n")
                end_program()

            except:
                print("Either the length or Breadth you Entered is not an Integer!!\n")
                choice()

        elif y == 2:
            if len(lst) != 0:
                try:
                    print("THE FOLLOWING IS A LIST OF EACH AVAILABLE RECTANGLE'S UNIQUE NUMBER")
                    for i in lst:
                        print(i)
                    print("\n")
                    a = int(input("Enter a unique number of your choice from the above listed: "))
                    if a in lst:
                        b = lst.index(a)
                        print("The details of Rectangle with that unique number are:\n"+" "+lst2[b]+"\n")
                        end_program()
                    else:
                        print("THE UNIQUE NUMBER YOU ENTERED DOES NOT EXIST\n")
                        choice()

                except:
                    print("THAT IS NOT A CORRECT UNIQUE CODE NUMBER!\n")
                    choice()
            else:
                print("YOU HAVE NOT CREATED ANY RECTANGLE YET\n")
                choice()
        else:
            print("Please Enter an assigned number\n")
            choice()

    except:
        print("That is not an Integer!!!\n")
        choice()


def end_program():
    try:  # keeps the program running until user enters an integer
        k = int(input("Enter Any Number To Continue | 0 To Exit\n"))
        if k == 0:
            print("Goodbye!!!")
        else:
            choice()

    except:  # keeps the program running until user enters an integer
        print("Please enter an integer")
        end_program()


choice()
