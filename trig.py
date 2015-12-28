#!/usr/bin/env python3
import math
import skilstak.colors as sc
        m = input("Type 'pi' for default 3.14, Otherwise set pi value. > ")
        if m == "pi":
def degtrig():
            pi = float(3.14)
            deg = float(input("degrees > "))
            z = float(deg * (pi/180))
            """z = radians"""
            """This mimics converting sin to a tangible number like a calculator, to 6 accurate decimal places"""
            zi = int(3 * 2 * 1)
            yi = int(5 * 4 * 3 * 2 * 1)
            xi= int(7 * 6 * 5 * 4 * 3 * 2 * 1)
            wi = int(9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
            vi = int(11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
            ui = int(13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
            z3 = float(z ** 3) 
            z5 = float(z ** 5) 
            z7 = float(z ** 7) 
            z9 = float(z ** 9) 
            z11 = float(z ** 11) 
            z13 = float(z ** 13)
            a = float(z3 / zi)
            b = float(z5 / yi)
            c = float(z7 / xi)
            d = float(z9 / wi)
            e = float(z11 / vi)
            f = float(z13 / ui)
            answera = float(z - a + b - c + d - e + f)
            answer = round(answera, 4)
            print("sin is",answer)
def hyptrig()
            """Sin = answer"""
            """answer is sin of the angle"""
            pi = float(3.14)
            deg = float(input("degrees > "))
            h = float(input("hypo length > "))   
            """gets x & y coordinates"""
            z = float(deg * (pi/180))
            zi = int(3 * 2 * 1)
            yi = int(5 * 4 * 3 * 2 * 1)
            xi= int(7 * 6 * 5 * 4 * 3 * 2 * 1)
            wi = int(9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
            vi = int(11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
            ui = int(13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
            z3 = float(z ** 3) 
            z5 = float(z ** 5) 
            z7 = float(z ** 7) 
            z9 = float(z ** 9) 
            z11 = float(z ** 11) 
            z13 = float(z ** 13)
            a = float(z3 / zi)
            b = float(z5 / yi)
            c = float(z7 / xi)
            d = float(z9 / wi)
            e = float(z11 / vi)
            f = float(z13 / ui)
            answera = float(z - a + b - c + d - e + f)
            answer = round(answera, 4)
            """z = radians"""
            """cross multiplies/ cancels hypotenuse with sin, to find side length of 'opposite', the side across from the hypotenuse"""
            r = float(h * answer)
            
            """(a)up & down is" = r"""
            print(
            """solves for 'b' using pythagoream theorem"""
            r2 = float(r * r)
            h2 = int(h * h)
            b2 = float(h2 - r2)
            if b2 == 0:
                bz = int(0)
                b = round(bz,4)
                print("b is",b)
            else:
                bz = abs(math.sqrt(b2))
                b = round(bz,4)
                """b is b """
