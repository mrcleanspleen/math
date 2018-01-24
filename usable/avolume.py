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

def vhexagon(base_edge, height):
    return (math.sqrt(3)*3) / 2 * base_edge**2 * height
    
def vhemisphere(rad):
    """Finds the volume of a hemisphere based on user input"""
    return (4/3 * 3.14 * rad**3) / 2

def vtriprism(base, tri_height, prism_height):
    """Finds the volume of a triangular prism"""
    return (base * tri_height) / 2 * prism_height

def voctahedron(edge):
    """Finds the Volume of an octahedron"""
    return edge**3 * math.sqrt(2) / 3

def vcylinder(rad, height):
    """Finds volume of a cylinder"""
    return rad**2 * 3.14 * height
