#!/usr/bin/python
# Date : 31/12/2018
# Author : Syed Abdullah Jelani
# Version : v.1
# Description : 4th Order Runge-Kutta Differential Eq. Solver.

import math
import os

os.chdir('C:\\Users\\Syed Abdullah Jelani\\Desktop\\PHYS200 PROJECTS\\FINAL')

x0=int(input("Enter a number for x0:"))
xfinal=int(input("Enter a number for xfinal:"))
y0 = int(input("Enter a number for y0:"))
interval= int(input("Enter the number of intervals between x0 and xfinal:"))
h= (xfinal - x0)/interval

def f(x0,y0):
    x = x0
    y = y0
    f =((5*x**2)-y)/(math.exp(x+y))
    return f



xstore =[x0]
ystore=[y0]




def rk4(h,x0,y0):
    x= x0
    y = y0
    for i in range(interval):
        F1= h *f(x,y)
        F2= h* f(x+(h/2),y+(F1/2))
        F3= h * f(x+(h/2),y+(F2/2))
        F4= h *f(x+h,y+F3)
        y = y + (1/6)*(F1 + (2*F2) + (2*F3) + F4)
        x+= h
        xstore.append(x)
        ystore.append(y)
    
    return xstore,ystore   


xstore , ystore = rk4(h,x0,y0)

def write_to_file(xstore,ystore):
    formatted_xstore = ["%.6f"%item for item in xstore]
    formatted_ystore = ["%.6f"%item for item in ystore]
    res = "\n".join("{} {}".format(x, y) for x, y in zip(formatted_xstore,formatted_ystore))
    output = res 
    file = open("S13.dat","w")
    file.write(str(output))
    file.close()

print(write_to_file(xstore,ystore))

###DONE###