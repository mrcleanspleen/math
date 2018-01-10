import skilstak.colors as c
import time as t
import math

'''
Many things have been simplified a lot. Lots of *very hard* work done by @rydens
'''

def solve_squareroot(num float)
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
def solve_compound():
    p = input("How much money did you borrow / invest ? >>> ")
    r = input("What was the interest rate in percent >>> ")
    t = input("How many years did you borrow/invest for? >>> ")
    v = input("How many times a year was it compounded? >>> ")
    vv = int(v)
    pp = int(p)
    rr = int(r)
    tt = int(t)
    """A = pp(1 + rr/1)^tt"""
    rr10 = int
    rr1 = int
    rr2 = int
    tr = int
    rr10 = rr / 100
    rr1 = rr10 / vv
    rr2 = 1 + rr1
    tv = int
    tv = tt * vv
    tr = rr2 ** tv
    y = int
    y = tr * pp
    print("You now have / owe",y)

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
