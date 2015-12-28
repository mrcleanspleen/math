#!/usr/bin/env python3
import skilstak.colors as c
def trig():
    print(c.cl + """
rd = radians to degrees
dr= degrees to radians""")
def welcome():
    print(c.clear + c.multi(""" 
                                                                                                                                 
 _ _ _     _                      _          _   _              _ _   _           _                  _         _     _           
| | | |___| |___ ___ _____ ___   | |_ ___   | |_| |_ ___    _ _| | |_|_|_____ ___| |_ ___    ___ ___| |___ _ _| |___| |_ ___ ___ 
| | | | -_| |  _| . |     | -_|  |  _| . |  |  _|   | -_|  | | | |  _| |     | .'|  _| -_|  |  _| .'| |  _| | | | .'|  _| . |  _|
|_____|___|_|___|___|_|_|_|___|  |_| |___|  |_| |_|_|___|  |___|_|_| |_|_|_|_|__,|_| |___|  |___|__,|_|___|___|_|__,|_| |___|_|  
                                                                                                                                         
    """))                                                                                                                                    

def intro():
    print("""What category?
    v = volume calculators
    g = graphing calculators
    m = other/ formulas
    a = area of 2-D shapes
    s = surface area calculators
    n = number calculators
    i = suggest something to add
    x to exit

    """)
def avolume():
    print(c.cl + """
    cu = volume of a cube,
    vrp = volume of rectangular pyramid
    vr = volume of rectangular prism
    sh = volume of a sphere,
    vtp = volume of a tri pyramid
    cv = cone volume
    vsp = square pyramid volume
    hm = hemisphere volume
    vh = hexagonal prism volume
    voc = volume of an octahedron
    vt = triangular prism volume
    vc = cylinder volume""")
def agraph():
    print(c.cl + """    
    GRAPHING
    is = inequality solver
    y = equation solver, 
    ss = system solver,
    si = system of inequalities""")
def asurface():
    print(c.cl + """
    hp = hexagonal prism surface area
    rp = rectangular pyramid surface area
    hs = hemisphere surface area
    sp = square pyramid surface area
    st = triangular prism surface area
    sc = cube surface area, 
    oc = octohedron surface area
    rs = rectangular prism surface area, 
    sps = sphere surface area
    cs = cylinder surface area,
    co = cone surface area
    tp = triangular pyramid surface area""")
def aarea():
    print(c.cl + """
    c = area of a circle
    s = area of a square, 
    tr = area of a triangle
    t = area of a trapezoid""")
def google():
    print("Copy this into your browser")
    print("""
https://www.google.com/search?espv=2&q=google+calculator&oq=google+cal
&gs_l=serp.1.1.0i131j0i20j0i10j0j0i131l2j0l4.51023.53960.0.55414.13.12.1.0.0.0.126.1233
.4j8.12.0....0...1c.1.64.serp..1.12.1159.0.ZZaV1XeCKhw""")
def exiting():
    print(c.clear + c.multi("Thanks for using the ultimate calculator!"))
    print(c.x + "Come again soon!")
    exit()
def amisc():
    print(c.cl + """
    pt = pythagorean theorem, 
    df = find distance between 2 points
    pc = perimeter of a circle
    sir = simple interest,
    ci = compound interest
    df = divide fractions
    mf = multiply fractions
    mul = multiply numbers
    pow = exponents and powers
    sr = square root a number""")
