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
            """z = radians"""
            """cross multiplies/ cancels hypotenuse with sin, to find side length of 'opposite', the side across from the hypotenuse"""
            r = float(h * answer)
            """(a)up & down is" = r"""
            """solves for 'b' using pythagoream theorem"""
            r2 = float(r * r)
            h2 = int(h * h)
            b2 = float(h2 - r2)
            if b2 == 0:
                bz = int(0)
                b = round(bz,4)
                print("b is",b)
                """finds the new X and Y coords"""
                newx = float(r + xcoord)
                newy = float(b + ycoord)
                print("Coordinate is",newx,",",newy)
            else:
                bz = abs(math.sqrt(b2))
                b = round(bz,4)
                """b is b """
                """finds the new X and Y coords"""
                newx = float(r + xcoord)
                newy = float(b + ycoord)
                print("Coordinate is",newx,",",newy)
                """finds slope"""
                slopey = float(newy - ycoord)
                slopex = float(newx - xcoord)
                if slopex == 0:
                    print("Vertical slope")
                elif slopey == 0:
                    print("Zero Slope")
                else:
                    rslope = float(slopey / slopex)
                    slope = round(rslope,4)
                    print("slope is",slope)

            """math.ceil(number) rounds up"""
            """copied from http://www.roguebasin.com/index.php?title=Bresenham%27s_Line_Algorithm""" 
            """Bresenham's Line Algorithm
            Produces a list of tuples from start and end
        
            >>> points1 = get_line((0, 0), (3, 4))
            >>> points2 = get_line((3, 4), (0, 0))
            >>> assert(set(points1) == set(points2))
            >>> print points1
            0, 0), (1, 1), (1, 2), (2, 3), (3, 4
            >>> print points2
            3, 4), (2, 3), (1, 2), (1, 1), (0, 0
            """
            """x1, y1 = start
            x2, y2 = end
            dx = x2 - x1
            dy = y2 - y1"""
            dx = abs(newx - xcoord)
            dy = abs(newy - ycoord)
            # Determine how steep the line is
            is_steep = abs(dy) > abs(dx)
        
            # Rotate line
            if is_steep:
                xcoord, ycoord = ycoord, xcoord
                newx, newy = newy, newx
        
            # Swap start and end points if necessary and store swap state
            swapped = int(0)
            if xcoord > newx:
                xcoord, newx = newx, xcoord
                ycoord, newy = newy, ycoord
            swapped = int(1)
        
            # Recalculate differentials
            dx = abs(newx - xcoord)
            dy = abs(newy - ycoord)
        
            # Calculate error
            error = abs(dx / 2.0)
            ystep = 1 if ycoord < newy else -1
            # Iterate over bounding box generating points between start and end
            y = float(ycoord)
            """rounds the new x coordniate"""
            rnewx = int(round(newx) - .5) + (newx > 0)
            points = []
            """for _ many x's calculates a y coordinates"""
            for x in range(xcoord, rnewx + 1):
                coord = (y, x) if is_steep else (x, y)
                points.append(coord)
                error -= abs(dy)
                if error < 0:
                    y += ystep
                    error += dx
        
            # Reverse the list if the coordinates were swapped
            if swapped == 1:
                points.reverse()
                print(points)
    except KeyboardInterrupt:
            print("goodbye")
            exit()
