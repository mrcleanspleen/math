import skilstak.colors as c 
import math
import time as t
def solve_cone():
    """Finds the volume of a cone"""
    height = input(c.cl + "What is the height of your cone? >>> ")
    radius = input(c.cl + "What is the radius of the base of your cone? >>> ")
    x = int(height)
    y = int(radius)
    answer = 3.14 * y**2 * x/3
    print("Your volume is : ",answer)

def solve_sqpyramid():
    base = input(c.cl + "What is the length of the base of your pyramid? >>> ")
    height = input(c.cl + "What is the height of your pyramid? >>> ")
    x = int(base)
    y = int(height)
    answer = x**2 * y/3
    print(c.cl + "Your answer is : ", answer)

def solve_cube():
    """Finds the volume of a cube"""
    height = input("What is the height of your cube? >>> ")
    x = int(height)
    answer = x**3
    print("Your volume is : " ,answer)

def solvesphere():
    """Finds the volume of a sphere based on user input"""
    radius = input("What is the radius of your sphere? >>> ")
    x = int(radius)
    print("pi = 3.14")
    answer = int(4/3 * 3.14 * x**3)
    print("Your volume is : ", answer)
def vsolve_rect():
    l = input("Length >>> ")
    w = input("Width >>> ")
    h = input("Height >>> ")
    ll = int(l)
    ww = int(w)
    hh = int(h)
    me = int
    me = ll * ww * hh
    print("Volume is",me)
def vrectpyramid():
    l = input("Length >>> ")
    w = input("Width >>> ")
    h = input("Height >>> ")
    ll = int(l)
    ww = int(w)
    hh = int(h)
    a = int
    a = ll * ww * hh / 3
    print("Volume is",a)
def vtripyramid():
    l = input("length of triangle >>> ")
    b = input("width of triangle >>> ")
    h = input("height of pyramid >>> ")
    ll = int(l)
    bb = int(b)
    hh = int(h)
    a = int
    a = 1 / 6
    c = int
    c  =  bb * hh * ll * a
    print("Volume is",c)
def vhexagon():
    a = input("Base edge >>> ")
    h = input("Height >>> ")
    aa = int(a)
    hh = int(h)
    w = int
    w = math.sqrt(3) * 3
    r = int
    r = w / 2 * aa * aa * hh
    print("Volume is",r)
def vhemisphere():
    """Finds the volume of a hemisphere based on user input"""
    radius = input("What is the radius of your hemisphere? >>> ")
    x = int(radius)
    print("pi = 3.14")
    answer = int(4/3 * 3.14 * x**3)
    v = int
    v = answer / 2
    print("Your volume is : ",v)
def vtriprism():
    a = input("Base of triangle >>> ")
    b = input("Height of triangle >>> ")
    c = input("Height of prism >>> ")
    aa = int(a)
    bb = int(b)
    cc = int(c)
    ab = int
    ab = aa * bb / 2
    ca = int
    ca = ab * cc
    print("Volume is",ca)
def voctahedron():
    a = input("Edge >>> ")
    aa = int(a)
    a3 = int
    a3 = aa * aa *aa
    x = int
    x = math.sqrt(2) / 3
    xa = int
    xa = x * a3
    print("Volume is",xa)
def vcylinder():
    a = input("Radius >>> ")
    b = input("Height >>> ")
    print("3.14 = pi")
    aa = int(a)
    bb = int(b)
    r = int
    r= aa *aa * 3.14 * bb
    print("Volume is",r)
