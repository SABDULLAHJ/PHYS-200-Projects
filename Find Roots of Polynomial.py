#!/usr/bin/python
# Date : 31/12/2018
# Author : Syed Abdullah Jelani
# Version : v.1
# Description : Find roots of a quadratic polynomial.

while True:
    input_list =[]
    
    while len(input_list) != 3:
        user_input = input("Enter three numbers separated by commas: ")
        input_list = user_input.split(',')
        if len(input_list) !=3 :
            print("Error! Enter only Three numbers seperated by commas!! Run again!")

    a= float(input_list[0])
    b= float(input_list[1])
    c= float(input_list[2])

    determinant = (b**2)-(4*a*c)


    def find_roots(a,b,c):
        if a ==0:
            return("Not a Quadratic polynomial")
        if determinant ==0 or (determinant) > 0   :
            x1 = ((-b) + (determinant**(1/2)))/(2*a)
            x2 = ((-b) - (determinant**(1/2)))/(2*a)
            if x1 !=x2:
                return("The roots are real: "+ str(x1) + " and "+ str(x2))
            else:
                return("There is a single real root: "+str(x1))
        else:
            x11 = str(float(-b /(2*a)))
            x12 = str(abs((determinant**(1/2))/(2*a))) + "i"
            x1 = x11 +"+" +x12
            x2 = x11 + "-"+x12
            return("The roots are imaginary: " + x1+ " and "+ x2)
        
    print(find_roots(a,b,c))
        

        
###DONE###