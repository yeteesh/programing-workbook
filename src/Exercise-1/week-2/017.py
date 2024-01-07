#Free Fall
'''Create a program that determines how quickly an object is travelling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume
that the acceleration

due to gravity is 9.8 m/s2 . You can use the formula vf = vi2 + 2ad to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.'''
import math
print('Enter the height which the object is going to be dropped, the height has to be in meters')
d = int(input()) 
vf = 0 + 9.8*d
print(vf) 
