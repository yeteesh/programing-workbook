## Sort 3 Integers
'''Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.'''
import math
print('Enter a number')
x = int(input())
print('Enter another number')
y = int(input())
print('Enter another number')
z = int(input())
print(min(x,y,z))
print('The number above is the smallest value of the three values you gave')
print(max(x,y,z))
print('The number above is the largest value of the three values you gave')
(x+y+z)-(min(x,y,z)+max(x,y,z))
print('The number above is the middle value of the three values you gave')
