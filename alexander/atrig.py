#!/usr/bin/env python3
import math as m
print("""
s = sin 
c = cos
t = tan           /|
                 / |
hypotenuse >>>  /  | <<< opposite
               /   |
              /____|        
                adjacent

sin = opposite / hypotenuse
cos = adjacent / hypotenuse
tan = opposite / adjacent
        """)
quest = input("Are you trying to find an angle or a side? ")
if "side" in quest:
    trig = input("cos, sin, or tan? ")
    ang = float(input("What is the measure of the angle? "))
    if "cos" in trig:
        side = input("Do you know hyp or adj? ")
        length = float(input("What is the length of that side? "))
        if "hyp" in side:
            sidlen = m.degrees(m.cos(ang)*length)
            print(str(sidlen))
        elif "adj" in side:
            sidlen = m.degrees(length/m.cos(ang))
            print(str(sidlen))
    elif "sin" in trig:
        side = input("Do you know opp or hyp? ")
        length = float(input("What is the legnth of that side? "))
        if "hyp" in side:
            sidlen = m.degrees(m.sin(ang)*length)
            print(str(sidlen))
        elif "opp" in side:
            sidlen = m.degrees(length/m.sin(ang))
            print(str(sidlen))
    elif "tan" in trig:
        side = input("Do you know opp or adj? ")
        length = float(input("What is the legnth of that side? "))
        if "adj" in side:
            sidlen = m.degrees(m.tan(ang)*length)
            print(str(sidlen))
        elif "opp" in side:
            sidlen = m.degrees(legnth/m.tan(ang))
            print(str(sidlen))
elif "angle" in quest:
    inv = input("inverse of cos, sin, or tan? ")
    if inv == "cos":
        adj = float(input("adjacent? "))
        hyp = float(input("hypotenuse? "))
        deg = m.degrees(m.acos(adj/hyp))
        print("x = " + str(deg))
    if inv == "sin":
        opp = float(input("opposite? "))
        hyp = float(input("hypotenuse? "))
        deg = m.degrees(m.asin(opp/hyp))
        print("x = " + str(deg))
    if inv == "tan":
        opp = float(input("opposite? "))
        adj = float(input("adjacent? "))
        deg = m.degrees(m.atan(opp/adj))
        print("x = " + str(deg))
      
