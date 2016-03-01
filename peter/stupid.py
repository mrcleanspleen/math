#!/usr/bin/env python3
import skilstak.colors as s
def mult():
    a = input(s.green + "?" + s.x + " * ? > ")
    b = int(input(a + " * ? > "))
    a1 = float(a)
    c = float(a1 * b)
    print("Your # is",c)
