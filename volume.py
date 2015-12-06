#!/usr/bin/env python3
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
    print(c.base03 + "Your volume is : ",answer)
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

