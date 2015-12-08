import skilstak.colors as c
import time as t
import math
import time as t
def solve_system():
    print("y = 1y,x = 1x,")
    print("No decimals, fractions, or 0/undefined slopes.")
    print("Make sure your equation is in slope-intercept form.")
    print("Enter y value please. Then hit enter.")
    print(c.green +" ?" + c.x + "y = ? x + ?")
    a1 = input(">>> ")
    print(c.clear + "Enter x value please. Then hit enter.")
    print(a1 + "y = " + c.green + "?" + c.x + "x + ?")
    a2 = input(">>> ")
    print(c.clear + "Enter last number. Then hit enter.")
    print(a1 + "y = " + a2 + "x + " + c.green + "?" + c.x)
    a3 = input(">>> ")
    y = int(a1)
    x = int(a2)
    if a3 == "0":
        b3 = int()
        b4 = int()
        b3 = y
        b4 = x
        b = int(a3)
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
        
def solve_system2():
    import skilstak.colors as c
    print(c.clear + c.x + "Welcome to the system pinpoint device.")
    print("1.Make sure you have 2 Systems")
    print("2.Make sure they are in Ax+By Form")
    print("3.Make sure you have no fractions or decimals")
    print("4.Make sure you have no undefined or zero slopes")
    print("First Equation")
    print("Enter A value then hit enter")
    print(c.green + "?" + c.x + "x + ?y = ?")
    print("?x + ?y = ?")
    f = input(">>> ")
    print(c.clear + "Enter B value then hit enter")
    print(f + "x + " + c.green + "?" + c.x + "y = ?")
    print("?x + ?y = ?")
    s = input(">>> ")
    print(c.clear + "Enter C value then hit enter")
    print(f  + "x + " + s + "y = " + c.green + "?")
    print(c.x + "?x + ?y = ?")
    t = input(">>> ")
    print(c.clear + "Second Equation")
    print("Enter A value then hit enter")
    print(f + "x + " + s + "y = " + t)
    print(c.green + "?" + c.x + "x + " + "?" + "y = " + "?")
    f1 = input(">>> ")
    print(c.clear + "Enter B value then hit enter")
    print(f + "x + " + s + "y = " + t)
    print(f1 + "x + " + c.green + "?" + c.x + "y = " + "?")
    s1 = input(">>> ")
    print(c.clear + "Enter C value then hit enter")
    print(f + "x + " + s + "y = " + t)
    print(f1 + "x + " + s1 + "y = " + c.green + "?" + c.x)
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
def yay():
    print("Your point works! Yay!")
def no():
    print("Your point does not work")
def solve_inequality2():
    """Checks whether a set of points will solve a systems of inequalities"""
    print(c.cl + c.base03 +  "Welcome to the system of inequalities solver machine")
    print("Make sure you have 2 inequalities")
    print("Make sure the equation is in standard form, or Ax + By = C")
    print("Make sure your have no fractions or decimals")
    print("Enter the first equations ineqaulity. Use only >, <, <=, or >=.")
    print(c.base03 + "?x + ?y " + c.red + "_ " + c.base03 + "?")
    in1 = input(">>> ")
    print(c.cl + "Enter A value then hit enter")
    print(c.red + "?" + c.base03 + "x + ?y " + in1 + " ?")
    a1 = input(">>> ")
    print(c.clear + "Enter B value then hit enter")
    print(c.base03 + a1 + "x + " + c.red + "?" + c.base03 + "y " + in1 + " ?")
    b1 = input(">>> ")
    print(c.clear + "Enter C value then hit enter")
    print(c.base03 + a1 + "x + " + b1 + "y " + in1 + c.red + " ?" + c.x)
    d1 = input(">>> ")
    print(c.cl + "Enter the second equations ineqaulity. Use only >, <, <=, or >=.")
    print(c.base03 + "?x + ?y " + c.red + "_ " + c.base03 + "?")
    in2 = input(">>> ")
    print(c.cl + "Enter A value then hit enter")
    print(c.red + "?" + c.base03 + "x + ?y " + in2 + " ?")
    a2 = input(">>> ")
    print(c.clear + "Enter B value then hit enter")
    print(c.base03 + a2 + "x + " + c.red + "?" + c.base03 + "y " + in2 + " ?")
    b2 = input(">>> ")
    print(c.clear + "Enter C value then hit enter")
    print(c.base03 + a2 + "x + " + b2 + "y " + in2 + c.red + " ?" + c.x)
    d2 = input(">>> ")
    print(c.cl + "What x value are you trying to test?")
    x = input(">>> ")
    print(c.cl + "What y value are you trying to test?")
    y = input(">>> ")
    a1 = int()
    a2 = int()
    b1 = int()
    b2 = int()
    d1 = int()
    d2 = int()
    x = int()
    y = int()
    answer1 = a1 * x + b1 * y
    answer2 = a2 * x + b2 * y
    if in1 == ">" and in2 == ">":
        if answer1 > d1 and answer2 > d2:
            yay()
        else:
            no()
    elif in1 == ">" and in2 == "<":
        if answer1 > d1 and answer2 < d2:
            yay()
        else:
            no()
    elif in1 == ">" and in2 == ">=":
        if answer1 > d1 and answer2 >= d2:
            yay()
        else:
            no()
    elif in1 == ">" and in2 == "<=":
        if answer1 > d1 and answer2 <= d2:
            yay()
        else:
            no()
    elif in1 == "<" and in2 == ">":
        if answer1 < d1 and answer2 > d2:
            yay()
        else:
            no()
    elif in1 == "<" and in2 == ">=":
        if answer1 < d1 and answer2 >= d2:
            yay()
        else:
            no()
    elif in1 == "<" and in2 == "<":
        if answer1 < d1 and answer2 < d2:
            yay()
        else:
            no()
    elif in1 == "<" and in2 == "<":
        if answer1 < d1 and answer2 < d2:
            yay()
        else:
            no()
    elif in1 == ">=" and in2 == ">":
        if answer1 >= d1 and answer2 > d2:
            yay()
        else:
            no()
    elif in1 == ">=" and in2 == "<":
        if answer1 >= d1 and answer2 < d2:
            yay()
        else:
            no()
    elif in1 == ">=" and in2 == ">=":
        if answer1 >= d1 and answer2 >= d2:
            yay()
        else:
            no()
    elif in1 == ">=" and in2 == "<=":
        if answer1 >= d1 and answer2 <= d2:
            yay()
        else:
            no()
    elif in1 == "<=" and in2 == ">":
        if answer1 <= d1 and answer2 > d2:
            yay()
        else:
            no()
    elif in1 == "<=" and in2 == ">=":
        if answer1 <= d1 and answer2 >= d2:
            yay()
        else:
            no()
    elif in1 == "<=" and in2 == "<":
        if answer1 <= d1 and answer2 < d2:
            yay()
        else:
            no()
    elif in1 == "<=" and in2 == "<":
        if answer1 <= d1 and answer2 < d2:
            yay()
        else:
            no()

def solve_inequality():
    """Checks whether a number will solve an inequality"""
    print(c.clear + c.x + "Welcome to the inequalities solver machine")
    print("Make sure your equation is in standard form, or Ax + By = C")
    print("Make sure you have no fractions or decimals")
    ine = input("Enter the inequality. Use >=, >, <, or <=. >>> ")
    print(c.x + "?x + ?y " + c.red + "_ " + c.x  + "?")
    print(c.clear + "Enter A value then hit enter")
    print(c.red + "?" + c.x + "x + ?y " + ine + " ?")
    a = input(">>> ")
    print(c.clear + "Enter B value then hit enter")
    print(c.x + a + "x + " + c.red + "?" + c.x + "y = ?")
    b = input(">>> ")
    print(c.clear + "Enter C value then hit enter")
    print(c.x + a + "x + " + b + "y " + ine + c.red + " ?" + c.x)
    d = input(">>> ")
    print(c.clear + "What x value are you trying to test?")
    x = input(">>> ")
    print(c.cl + "What y value are you trying to test ?")
    y = input(">>> ")
    a = int()
    x = int()
    b = int()
    y = int()
    d = int()
    answer = a * x + b * y
    if ine == ">":
        if answer > d:
            yay()
        else:
            no()
    elif ine == "<":
        if answer < d:
            yay()
        else:
            no()
    elif ine == ">=":
        if answer >= d:
            yay()
        else:
            no()
    elif ine == "<=":
        if answer <= d:
            yay()
        else:
            no()
    else:
        print("ERROR! ERROR! DOES NOT COMPUTE! KABLOOEY!")

