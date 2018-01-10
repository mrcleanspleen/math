#!/usr/bin/env/python3
import skilstak.colors as c
import math
def choose_area():
    print(c.cl + """
    c = area of a circle
    s = area of a square, 
    tr = area of a triangle
    t = area of a trapezoid""")
    inpt = input(">>> ")
    if inpt == "s":
        solve_square()
    elif inpt == "c":
        solve_circle()
    elif inpt == "tr":
        solve_triange()
    elif inpt == "t":
        solve_trapazoid()
    else:
        print(c.cl + "Human. Y you do dis.")
def solve_square(x float):
    """Finds the area of a square based on its height"""
    answer = x * x
    return answer

def solve_circle(rad float):
    """Finds the area of a circle based on its radius"""
    answer = rad * rad * 3.14
    return answer
def solve_triangle(height float, length float):
    """Finds the area of a traingle based on its height and base"""
    answer = height * length/2
    return answer
def solve_trapazoid(len1 float, len2 float, height float):
    """Finds the area of a trapazoid"""
    answer = len1 * len2/2 * height
    return answer
