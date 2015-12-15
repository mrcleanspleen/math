#!/usr/bin/env/python3
import skilstak.colors as c
import math

def solve_square():
    """Finds the area of a square based on its height"""
    x = int(input("What is the height of your square? >>> "))
    answer = int()
    answer = x * x
    print("Your answer is : ",answer)

def solve_circle():
    """Finds the area of a circle based on its radius"""
    x = int(input("What is the radius of your circle? >>> "))
    answer = x * x * 3.14
    print("Your answer is : " + str(answer))

def solve_triangle():
    """Finds the area of a traingle based on its height and base"""
    x = int(input("What is the height of your triangle? >>> "))
    y = int(input("What is the length of the base of your triangle? >>> "))
    answer = int()
    answer = x * y/2
    print("Your answer is : " + str(answer))

def solve_trapazoid():
    """Finds the area of a trapazoid"""
    x = int(input("What is the length of the first base? >>> "))
    y = int(input("What is the length of the second base? >>> "))
    z = int(input("What is the height of the trapazoid? >>> "))
    answer = int()
    answer = x * y/2 * z
    print("Your answer is : " + str(answer))
