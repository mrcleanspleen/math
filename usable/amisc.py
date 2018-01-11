import skilstak.colors as c
import time as t
import math

'''
Many things have been simplified a lot. Lots of *very hard* work done by @rydens
'''

def solve_squareroot(num float):
    """Finds the square root of a number"""
    return math.sqrt(num)

def solve_distance(x2 float, x1 float, y2 float, y1 float):
    return float(math.sqrt(((x2-x1) ** 2) + ((y2-y1) ** 2)))

def solve_slope(y2 float, y1 float, x2 float, x1 float):
    return float((y2 - y1)/(x2-x1))

def solve_percircle(b float):
    return (3.14 * 2 * b)
def solve_py(a = 0.0, b = 0.0, c = 0.0):
    if a == 0.0 or b == 0.0:
        return math.sqrt((c ** 2) - (a ** 2) - (b ** 2))
    elif answer == "c":
        return math.sqrt((a ** 2) + (b ** 2))

def solve_interest():
    p = input("How much money did you borrow / invest ? >>> ")
    r = input("What was the interest rate in percent (Must be at least 1) >>> ")
    t = input("How many years did you borrow for? >>> ")
    pp = int(p)
    rr = int(r)
    tt = int(t)
    rrr = int
    rrr = rr / 100
    a = int
    a = pp * rrr * tt
    print("Interest amount is",a)
    b = int
    b = a + pp
    print("You now owe",b)

def solve_compound(prin float, rate float, time float, comp float):
    return (prin*(1+(rate/comp)**(comp*time)

def power(num int, exp int):
    return num ** exp

def mulfrac(num1 int, de1 int, num2 int, de2 int):
    return str(num1 * num2) + '/' + str(de1 * de2)

def divfrac():
    a = input("( " + c.green + "? " + c.x + " / ?) / ( ? / ? ) >>> ")
    b = input("( " + a + c.x + " /" + c.green + " ? " + c.x + ") / ( ? / ? ) >>> ")
    c1 = input("( " + a + c.x + " / " + b + " ) / (" + c.green + " ? " + c.x + "/ ? ) >>> ")
    d = input("( " + a + c.x + " / " + b + " ) / ( " + c1 + " /" + c.green + " ? " + c.x + ") >>> ")
    a1 = int(a)
    b1 = int(b)
    c2 = int(c1)
    d1 = int(d)
    x = int
    x = a1 * d1
    y = int
    y = b1 * c2
    print("Your fraction is",x,"/",y)
def user():
    print("Type what you want to be added, then type anything");
    x = 'user.txt'
    with open (x, "w") as f:
        f.write (input (">>> "));
if __name__ == '__main__':
    solve_compound(100, .02, 5, 2)
