import skilstak.colors as c
import time as t
import math
def prime():
    option = input(c.clear + "o = fast calc; n = normal >>> ")
    if option == "o":
        i = int(input("what odd # to start at? > ")) 
        while True:
            squared_i = math.sqrt(i)
            ri = math.ceil(squared_i)
            is_prime = True
            for j in range(2,ri):
                if i%j == 0: #Says if there is a remainder
                    is_prime = False
                    break
            if is_prime == True:
                print(i)
            i += 2 #Adds one to i
        if option == "n":
            i = int(input("what # to start at? > ")) 
            while True:
                squared_i = math.sqrt(i)
                ri = math.ceil(squared_i)
                is_prime = True
                for j in range(2,ri):
                    if i%j == 0: #Says if there is a remainder
                        is_prime = False
                        break
                if is_prime == True:
                    print(i)
                    i += 1 #Adds one to i
        else:
            print("choose one option")
def test_prime():
    i = int(input("what # to test? > "))
    squared_i = math.sqrt(i)
    ri = math.ceil(squared_i)
    if i < 3:
        print("too small")
        exit()
    elif i <= 16:
        ri = i
    is_prime = True
    for j in range(2,ri):
        if i%j == 0: #Says if there is a remainder
            is_prime = False
    if is_prime == True:
        print("Is prime")
    else:
        print("Not prime")
def solve_squareroot():
    """Finds the square root of a number"""
    inpu = input("square root what number? >>> ")
    i = int(inpu)
    answer = int
    answer = math.sqrt(i)
    print("square root is",answer)
def solve_distance():
    print(""" 
    (x, y) and (x, y)
    ⇩  ⇩       ⇩  ⇩
    x1 y1      x2 y2""")
    xa = input("x1 >>> ")
    ya = input("y1 >>> ")
    xb = input("x2 >>> ")
    yb = input("y2 >>> ")
    x1 = int(xa)
    y1 = int(ya)
    x2 = int(xb)
    y2 = int(yb)
    x3 = int
    x3 = x2 - x1
    y3 = int
    y3 = y2 - y1
    x4 = int
    x4 = x3 * x3 + y3 * y3
    x5 = int
    x5 = math.sqrt(x4)
    print("Distance between the two points is",x5)
def solve_slope():
    print(""" 
    (x, y) and (x, y)
    ⇩  ⇩       ⇩  ⇩
    x1 y1      x2 y2""")
    xa = input("x1 >>> ")
    ya = input("y1 >>> ")
    xb = input("x2 >>> ")
    yb = input("y2 >>> ")
    x1 = int(xa)
    y1 = int(ya)
    x2 = int(xb)
    y2 = int(yb)
    y3 = int
    y3 = y2 - y1
    x3 = int
    x3 = x2 - x1
    yx = int
    yx = y3 / x3
    print("Slope is",yx)

def solve_percircle():

    b = input("radius >>> ")
    c = int(b)
    a = int
    a = 3.14 * 2 * c
    print(a)
def solve_py():
    print("""
             |\ 
             | \ 
             |  \c
            a|   \ 
             |    \ 
             |     \ 
             |______\ 
                b   """)
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
def power():
    a = input(c.green + " ? " + c.x + "^ ? >>> ")
    b = input(a + " ^ " + c.green + "?" + c.x + " >>> ")
    aa = int(a)
    bb = int(b)
    d = int
    d = aa ** bb
    print("Your number is",d)
def mulfrac():
    a = input("( " + c.green + "?" + c.x + " / ?) * ( ? / ? ) >>> ")
    b = input("( " + a + c.x + " /" + c.green + " ? " + c.x + ") * ( ? / ? ) >>> ")
    c1 = input("( " + a + c.x + " / " + b + " ) * (" + c.green + " ? " + c.x + "/ ? ) >>> ")
    d = input("( " + a + c.x + " / " + b + ") * ( " + c1 + " /" + c.green + " ? " + c.x + ") >>> ")
    a1 = int(a)
    b1 = int(b)
    c2 = int(c1)
    d1 = int(d)
    x = int
    x = a1 * c2
    y = int
    y = b1 * d1
    print("Your fraction is",x,"/",y)
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
