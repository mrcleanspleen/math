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
        print("a value is",cb3)
    elif answer == "b":
        e = input("a value >>> ")
        r = input("c value >>> ")
        b = int(e)
        c = int(r)
        a = int
        b1 = int
        c1 = int
        b1 = b * b
        c1 = c * c
        cb2 = int
        cb2 = c1 - b1
        cb3 = int
        cb3 = math.sqrt(cb2)
        print("b value is",cb3)
    elif answer == "c":
        t = input("a value >>> ")
        y = input("b value >>> ")
        a = int(t)
        b = int(y)
        a1 = int
        b1 = int
        a1 = a * a
        b1 = b * b
        ab11 = int
        ab11 = a1 + b1
        c = math.sqrt(ab11)
        print("c value is",c)
def solve_system2():
    import skilstak.colors as c
    print(c.clear + c.base03 + "Welcome to the system pinpoint device.")
    print("1.Make sure you have 2 Systems")
    print("2.Make sure they are in Ax+By Form")
    print("3.Make sure you have no fractions or decimals")
    print("4.Make sure you have no undefined or zero slopes")
    print("First Equation")
    print("Enter A value then hit enter")
    print(c.green + "?" + c.base03 + "x + ?y = ?")
    print("?x + ?y = ?")
    f = input(">>> ")
    print(c.clear + "Enter B value then hit enter")
    print(f + "x + " + c.green + "?" + c.base03 + "y = ?")
    print("?x + ?y = ?")
    s = input(">>> ")
    print(c.clear + "Enter C value then hit enter")
    print(f  + "x + " + s + "y = " + c.green + "?")
    print(c.base03 + "?x + ?y = ?")
    t = input(">>> ")
    print(c.clear + "Second Equation")
    print("Enter A value then hit enter")
    print(f + "x + " + s + "y = " + t)
    print(c.green + "?" + c.base03 + "x + " + "?" + "y = " + "?")
    f1 = input(">>> ")
    print(c.clear + "Enter B value then hit enter")
    print(f + "x + " + s + "y = " + t)
    print(f1 + "x + " + c.green + "?" + c.base03 + "y = " + "?")
    s1 = input(">>> ")
    print(c.clear + "Enter C value then hit enter")
    print(f + "x + " + s + "y = " + t)
    print(f1 + "x + " + s1 + "y = " + c.green + "?" + c.base03)
    t1 = input(">>> ")
    print(c.clear + "Solving the systems:" + f + " x + " + s + " y = " + t)
    print("and " + f1 + " x + " + s1 + " y = " + t1) 
    a = int(f)
    b = int(s)
    c = int(t)
    d = int(f1)
    e = int(s1)
    f = int(t1)
    ad = int
    ae = int
    af = int
    d1a = int
    d1b = int
    d1c = int
    d1 = int
    aed1b = int
    d1caf = int
    y = int 
    by = int
    by1 = int
    cby1 = int
    x = int
    ad = a * d
    ae = a * e
    af = a * f
    d1 = d * -1
    d1a = d1 * a
    d1b = d1 * b
    d1c = d1 * c
    aed1b = ae + d1b
    d1caf = d1c + af
    """if no solution or infinite, float error division line 77"""
    y = 1. * d1caf / aed1b
    by = b * y
    by1 = by * -1
    cby1 = c + by1
    x = 1. * cby1 / a
    print("The systems intersect at", x,",",y)
def parse_args():
    import sys
    option = ""
    if len(sys.argv) == 2:
        if sys.argv[1].startswith("-"):
            option = sys.argv[1]
        else:
            print("ERROR! ERROR! DOES NOT COMPUTE! KABLOOOEY!")
