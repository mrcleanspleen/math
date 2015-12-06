#!/usr/bin/env/python3
import skilstak.colors as c
import math
import time as t

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
