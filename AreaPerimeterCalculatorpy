# This program calculates the perimeter and area of a circle, equilateral triangle, square,
# and rectangle. The program should shows the assigned number for each shape to the user
# This program makes sure that the user to enters an assigned number choice
# Then the program asks for the length of the triangle or square, or the radius of the circle,
# or the two sides of the rectangle. For the triangle, it asks for the side
# The program continues to run till the user wants to quit.
# Inputs = The user types in the values for either the side of a triangle, the length of a square,
# the length and breadth of a rectangle, or the radius or diameter of a circle.
# Outputs = The program prints out the perimeter and area of the chosen shape (triangle, rectangle,
# circle or square).


import math     # this imports the math library.


def main():
    intro_self()
    shape_choice()

def intro_self():
    name_user = input("Hey! What is your name? ")
    print("WELCOME", name_user.upper()+"!!!", "See below the number assigned to each shape!")

def shape_choice():
    n = int(input("1 = Triangle \n2 = Circle \n3 = Rectangle \n4 = Square \n0 = Exit Program"
                  "\nENTER THE NUMBER ASSIGNED TO THE SHAPE YOU WISH TO FIND ITS AREA AND PERIMETER: "))
    # this takes the user's input for what assigned shape they choose to work on.

    if n == 1:
        def calc_triangle():
            side = int(input("Enter the Side length of the Triangle: "))
            area_of_triangle = (math.sqrt(3) * (side ** 2) / 4)
            perimeter_of_triangle = (3 * side)
            return print("Area of Triangle: ",str(area_of_triangle)), \
                print("Perimeter of Triangle: ", str(perimeter_of_triangle))
        calc_triangle()    # this function is where the calculation for the area and perimeter of a triangle takes place
        shape_choice()   # this calls backs the shape_choice function and restarts the program.

    elif n == 2:
        def circle_calc():
            g = int(input("Do you have the radius or diameter? Enter 1 for Radius and 2 for Diameter: "))
            if g == 1:
                radius = int(input("Enter the Radius of the Circle: "))
                area_of_circle = (math.pi * (radius ** 2))
                perimeter_of_circle = (2 * math.pi * radius)
                return print("Area of Circle:", str(area_of_circle)), \
                    print("Circumference of Circle:", str(perimeter_of_circle))
            elif g == 2:
                diameter = int(input("Enter the Diameter of the Circle: "))
                dia_to_radius = (diameter / 2)
                area_dia_circle = (math.pi * (dia_to_radius ** 2))
                perimeter_dia_circle = (2 * math.pi * dia_to_radius)
                return print("Area of Circle: ", str(area_dia_circle)), \
                    print("Circumference of Circle: ",str(perimeter_dia_circle))
            else:
                print("You Entered an Unassigned Number")
                circle_calc()
        circle_calc()   # this function is where the calculation of circle is done
        shape_choice()  # calls back the shape_choice function so the program doesn't stop running

    elif n == 3:
        def calc_rectangle():
            length = int(input("Enter the Length of the Rectangle: "))
            breadth = int(input("Enter the Breadth of the Rectangle: "))
            area_of_rectangle = (length * breadth)
            perimeter_of_rectangle = ((2 * length)+(2 * breadth))
            return print("Area of Rectangle:", str(area_of_rectangle)), \
                print("Perimeter of Rectangle:", str(perimeter_of_rectangle))
        calc_rectangle()  # this is where the calculation for rectangle is done
        shape_choice()  # this calls back the shape_choice function

    elif n == 4:
        def calc_square():
            l_square = int(input("Enter the Length of the Square: "))
            area_of_square = (l_square ** 2)
            perimeter_of_square = (4 * l_square)
            return print("Area of Square:", str(area_of_square)), \
                print("Perimeter of Square:", str(perimeter_of_square))
        calc_square()   # this is the calculation for the square's area and perimeter
        shape_choice()  # calls back the shape_choice function to restart the program from user's choice part

    elif n == 0:
        return print("Goodbye!")    # prints goodbye to the screen

    else:
        print("YOU ENTERED AN UNASSIGNED NUMBER \nPLEASE ENTER A CORRECT NUMBER")
        shape_choice()  # makes the program keep running while the user enters a wrong choice


# running code
main()
