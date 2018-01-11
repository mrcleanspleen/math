import skilstak.colors as c 
import math
import time as t
def solve_cone(height, rad):
    """Finds the volume of a cone"""
    return float(3.14 * rad**2 * height/3)

def solve_sqpyramid(base, heigh):
    return float(base**2 * height/3)

def solve_cube(height):
    """Finds the volume of a cube"""
    return float(height**3)

def solvesphere(rad):
    """Finds the volume of a sphere based on user input"""
    return float(4/3 * 3.14 * rad**3)

def vsolve_rect(leng, wid, ht):
    return float(leng * wid * ht)

def vrectpyramid(leng, wid, ht):
    return leng * wid * ht / 3

def vtripyramid(leng, wid, ht):
    return (leng * wid * ht)/6

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
