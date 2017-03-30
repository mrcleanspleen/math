#!/usr/bin/env python3
import math as m
print("""
s = sin 
c = cos
t = ta            /|
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
    if trig == "cos":
        adj = input("adjacent? ")
        hyp = input("hypotenuse? ")
if "angle" in quest:
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
      
