#!/usr/bin/env python3
import skilstak.colors as c
import math    
def paint_cost():
    """Determines how much it would cost to paint the outside surface of an
    object based on surface area, cost per gallon, and how much 1 gallon
    of paint covers, in sq. ft.
    """
    q = input(c.cl + "Do you want to sove how much it will cost to paint the surface of the object? >>> ")
    if ["yes","y","sure"] in q:
        print(c.cl + "What is the surface area of the object?")
        sa = int(input(">>> "))
        print(c.cl + "How many sq. units can one gallon cover?")
        g = int(input(">>> "))
        print(c.cl + "How much does one gallon cost?")

def sacube():
    a = int(input("What is one side's length of the cube? >>> "))
    b = int
    answer = a * a * 6
    print("The surface area of the cube is",b)
def satriprism():
    q = input("y = right triangle, n otherwise >>> ")
    if q == "y":
        a = int(input("Base of triangle >>> "))
        b = int(input("Height of triangle >>> "))
        c = int(input("Length of Triangular Prism >>> "))
        a2 = int
        b2 = int
        ab2 = int
        d = int
        w = int
        w = a * b
        a2 = a * a
        b2 = b * b
        ab2 = a2 + b2
        d = math.sqrt(ab2)
        abc3 = int
        abc3 = d * c
        ac = int
        ab = int
        ac = a * c
        ab = b * c
        r = int
        r = ac + ab + abc3 + w
        print("Surface area of triangular prism is ",r)    
    elif q == "n":
        print("""
               /\ 
              /  \ 
           A /    \ B
            /      \ 
           /________\ 
                C
                
        """)
        A = input("A >>> ")
        B = input("B >>> ")
        C = input("C >>> ")
        u = input("Height of triangular Prism >>> ")
        aa = int(A)
        bb = int(B)
        cc = int(C)
        uu = int(u)
        p1 = int
        p1 = aa + bb + cc
        p = int
        p = p1 / 2
        pa = int
        pb = int
        pc = int
        pa = p - aa
        pb = p - bb
        pc = p - cc
        b = int
        b = p * pa * pb * pc
        b2 = int
        b2 = math.sqrt(b)
        if b2 == 0:
            print("impossible triangle")
        else:
            b3 = int
            p2 = int
            bp = int
            b3 = b2 * 2
            p2 = p1 * uu
            bp = b3 + p2
            print("surface areas is ≈",bp)
def rectsurface():
    l = input("Length >>> ")
    w = input("Width >>> ")
    h = input("Height >>> ")
    ll = int(l)
    ww = int(w)
    hh = int(h)
    hw = int
    wl = int
    hl = int
    hw = ww * hh
    wl = ww * ll
    hl = hh * ll
    total = int
    total = hw + wl + hl
    total1 = int
    total1 = 2 * total
    print("Surface area is",total1)
def spheresurface():
    r = input("radius >>> ")
    rr = int(r)
    rrr = int
    rrr = rr * rr
    print("3.14 is pi")
    a = int
    a = rrr * 4 * 3.14
    print("Surface area is",a)
def cylindersurface():
    r = input("radius >>> ")
    h = input("height >>> ")
    rr = int(r)
    hh = int(h)
    q = int
    print("3.14 = pi")
    q = 2 * 3.14 * rr * hh
    u = int
    u = 2 * 3.14 * rr * rr
    qu = int
    qu = u + q
    print("Surface area is",qu)
def squarepyramid():
    a = input("Base edge >>> ")
    h = input("Height >>> ")
    aa = int(a)
    hh = int(h)
    aa2 = int
    hh2 = int
    aa2 = aa * aa
    hh2 = hh * hh
    aa4 = int
    aa4 = aa2 / 4
    ah = int
    ah = aa4 + hh2
    sah = int
    sah = math.sqrt(ah)
    sah2 = int
    sah2 = 2 * aa * sah
    answer = int
    answer = sah2 + aa2
    print("Surface area is",answer)
def rectpyramid():
    l = input("length >>> ")
    w = input("width >>> ")
    h = input("height >>> ")
    ll = int(l)
    ww = int(w)
    hh = int(h)
    lw = int
    lw = ll * ww
    ww2 = int
    ww22 = int
    ll2 = int
    ll22 = int
    ww2 = ww / 2
    ww22 = ww2 * ww2
    ll2 = ll / 2
    ll22 = ll2 * ll2
    h2 = int
    h2 = hh * hh
    hl = int
    hl = h2 + ll22
    shl = int
    shl = math.sqrt(hl)
    wshl = int
    wshl = ww * shl
    hw = int
    hw = h2 + ww22
    shw = int
    shw = math.sqrt(hw)
    lshw = int
    lshw = ll * shw
    answer = int
    answer = lshw + wshl + lw
    print("Surface area is",answer)
def tripyramid():
    b = input("Side of base >>> ")
    a = input("Apothem (height of triangle) >>> ")
    l = input("slant height >>> ")
    bb = int(b)
    aa = int(a)
    ll = int(l)
    ba2 = int
    ba2 = bb * aa * .5
    bl = int
    bl = 1.5 * bb * ll
    blab = int
    blab = bl + ba2
    print("surface area is",blab)
def conesurface():
    r = input("Radius >>> ")
    h = input("Height >>> ")
    print("3.14  = pi")
    rr = int(r)
    hh = int(h)
    rh = int
    rh = hh * hh + rr * rr
    srh = int
    srh = math.sqrt(rh)
    rs = int
    rs = rr + srh
    pir = int
    pir = rr * 3.14 * rs
    print("Surface area is",pir)
def octahedron():
    a = input("Edge >>> ")
    aa = int(a)
    aa2 = int
    aa2 = aa * aa
    sr = int
    sr = math.sqrt(3)
    sr2 = int
    sr2 = aa2 * sr * 2
    print("Surface area is",sr2)
def hemisphere():
    r = input("radius >>> ")
    print("3.14 = pi")
    rr = int(r)
    rrr = int
    rrr = rr * rr * 2 * 3.14
    print("Surface area is",rrr)
def hexagon():
    a = input("Base edge >>> ")
    h = input("Height >>> ")
    aa = int(a)
    hh = int(h)
    ah = int
    ah = aa * hh * 6 + 3 * math.sqrt(3) * aa * aa
    print("Surface area is",ah)
