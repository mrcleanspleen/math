#!/usr/bin/env python3
import skilstak.colors as c 
import math
import time as t

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

