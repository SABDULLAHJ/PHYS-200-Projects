#!/usr/bin/python
# Date : 31/12/2018
# Author : Syed Abdullah Jelani
# Version : v.1
# Description : Convert image from RGB to grayscale.

import os
os.chdir("C:/Users/Syed Abdullah Jelani/Desktop/RGB to grayscale converter pics")

from PIL import Image


im = Image.open('einstein3.jpg')
im.show()
pix = im.load()
test_copy = pix
size= im.size  
#print (pix[1,1])  


for x in range(0,size[0]):
    for y in range(0,size[1]):
        Red = test_copy[x,y][0]
        Blue =test_copy[x,y][1]
        Green= test_copy[x,y][2]
        Gray = (Red * 0.3 + Green * 0.59 + Blue * 0.11)
        #test_copy[x,y] = ((int(a*0.3)),int(b*0.59),int(c*0.11)) grayscale1 copy
        test_copy[x,y] = ((int(Gray)),int(Gray),int(Gray))# Set the RGBA Value of the image (tuple)
        

im.show()

###DONE###