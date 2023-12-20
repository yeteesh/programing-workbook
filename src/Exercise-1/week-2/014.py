## Area and Volume
'''Write a program that begins by reading a radius, r , from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r . Use the pi constant in the math module in your
calculations.
##Hint:Hint: The area of a circle is computed using the formula area = πr 2 . The
volume of a sphere is computed using the formula volume = 43 πr 3 .'''
import math
print(' Enter the Radius of a circle')
x = int(input())
print(x*x)
print('this is the area of the circle')
print(4/3*math.pi*x*3)
print('this is the volume of the sphere')
