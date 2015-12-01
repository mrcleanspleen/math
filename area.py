import skilstak.colors as c
import time as t
import math
def solve_square():
    """Finds the area of a square based on its height"""
    height = input("What is the height of your square? >>> ")
    x = int(height)
    answer = int()
    answer = x * x
    print("Your answer is : ",answer)

def solve_circle():
    """Finds the area of a circle based on its radius"""
    radius = input("What is the radius of your circle? >>> ")
    x = int(radius)
    answer = int()    
    answer = x * x * 3.14
    print("Your answer is : " + str(answer))

def solve_triangle():
    """Finds the area of a traingle based on its height and base"""
    height = input("What is the height of your triangle? >>> ")
    base = input("What is the length of the base of your triangle? >>> ")
    x = int(height)
    y = int(base)
    answer = int()
    answer = x * y/2
    print("Your answer is : " + str(answer))

def solve_trapazoid():
    """Finds the area of a trapazoid"""
    base1 = input("What is the length of the first base? >>> ")
    base2 = input("What is the length of the second base? >>> ")
    height = input("What is the height of the trapazoid? >>> ")
    x = int(base1)
    y = int(base2)
    z = int(height)
    answer = int()
    answer = x * y/2 * z
    print("Your answer is : " + str(answer))
def solve_system():
    print(c.clear + c.green +"Welcome to the Math System Solver!")
    print("y = 1y,x = 1x,")
    print("No decimals, fractions, or 0/undefined slopes.")
    t.sleep(3)
    """DIRECTIONS"""
    print(c.clear + c.x + c.base03 + "Make sure your equation is in slope-intercept form.")
    print("Enter y value please. Then hit enter.")
    print(c.green +" ?" + c.base03 + "y = ? x + ?")
    a1 = input(">>> ")
    print(c.clear + "Enter x value please. Then hit enter.")
    print(a1 + "y = " + c.green + "?" + c.base03 + "x + ?")
    a2 = input(">>> ")
    print(c.clear + "Enter last number. Then hit enter.")
    print(a1 + "y = " + a2 + "x + " + c.green + "?" + c.base03)
    a3 = input(">>> ")
    y = int(a1)
    x = int(a2)
    if a3 == "0":
        b3 = int()
        b4 = int()
        b3 = y
        b4 = x
        b = int(a3)
        p4()
        x1 = int()
        b1 = int()
        x1 = 1. * x / y
        b1 = 1. * b / y
        print("slope is",x1)
        print("y int is 0 ,",b1)
        x2 = int()
        b2 = int()
        x2 = x * -1
        b2 = 1. * b / x2
        b5 = int()
        b6 = int()
        b5 = b3 + b3
        b6 = b4 + b4
        print("x intercept is",b2,", 0")
        print("3 points to plot are:0 ,",b1,"and",b3,",",b4,"and",b5,",",b6)
        print("This is direct variation.")
    else:
        b = int(a3)
        print(c.clear + "Solving the system:")
        print(a1," y = ",a2," x + ",a3)
        x1 = int()
        b1 = int()
        """zero division error"""
        x1 = 1. * x / y
        b1 = 1. * b / y
        print("slope is",x1)
        print("y int is 0 ,",b1)
        x2 = int()
        b2 = int()
        x2 = x * -1
        b2 = 1. * b / x2
        print("x intercept is",b2,", 0")
        b3 = int()
        b31 = int()
        b4 = int()
        b3 = b1 + b1
        b31 = b2 - b2
        b4 = b31 - b2
        print("3 points to plot are:0 ,",b1,"and",b2,", 0 and",b4,",",b3)
def solve_py():
    print("  |\ ")
    print("  | \ ")
    print("  |  \c")
    print(" a|   \ ")
    print("  |    \ ")
    print("  |     \ ")
    print("  |______\ ")
    print("      b    ")
    print("What side are you missing?")
    answer = input(">>> ")
    if answer == "a":
        q = input("b value >>> ")
        w = input("c value >>> ")
        b = int(q)
        c = int(w)
        a = int
        b1 = int
        c1 = int
        b1 = b * b
        c1 = c * c
        cb2 = int
        cb2 = c1 - b1
        cb3 = int
        cb3 = math.sqrt(cb2)
        print(cb3)
def parse_args():
    import sys
    option = ""
    if len(sys.argv) == 2:
        if sys.argv[1].startswith("-"):
            option = sys.argv[1]
        else:
            print("ERROR! ERROR! DOES NOT COMPUTE! KABLOOOEY!")
