import skilstak.colors as c
import time as t
from sys import argv
import math
def solve_cube():
    """Finds the volume of a cube"""
    x = input("What is the height of your cube? >>> ")
    x = int()
    answer = math.pow(x, 4)
    print("Your answer is : " ,answer)
