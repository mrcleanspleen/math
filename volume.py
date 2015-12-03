import skilstak.colors as c
import time as t
from sys import argv
import math
def solve_cube():
    """Finds the volume of a cube"""
    x = input("What is the height of your cube? >>> ")
    x = float()
    answer = float(x**2)
    print("Your answer is : " ,answer)

def solve_sphere():
    """Finds the volume of a sphere based on user input"""
    x = input("What is the radius of your sphere? >>> ")
    x = int()
    xpower = math.pow(x, 3)
    answer = int(4/3 * 3.14 * xpower)
    print("Your answer is : ", answer)
