# -*- coding: utf-8 -*-
"""
This is just a small test code on using a code that consists of RBG values, in which we use a formula to determine the actual RGB Values.
"""

def closestColor(pixels):
    # Write your code here
    
    Rb =  pixels[0][0:8]
    Gb = pixels[0][8:16]
    Bb = pixels[0][16:24]
    R = 0
    G = 0
    B = 0
    
    for i in Rb:
        R = R*2 + int(i)
    for j in Gb:
        G = G*2 + int(j)
    for k in Bb:
        B = B*2 + int(k) 
        
   

    

    return R,G,B


pixels = ["000000001111101100000110"]

print(closestColor(pixels))   
    
