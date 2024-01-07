## Volume of a Cylinder
'''The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.'''
print('Enter the raidus of the cylinder ')
x = int(input()) 
print('if the raidus is a decimal value then enter it')
w = float(input())
print('Enter the height of the cylinder')
y = int(input())
print('If the raidus is a decimal value then enter it')
a = float(input())
v = x*y
print(v*y)
z = w*a
b = z*a
if b > (z+0.5):
    print(z)
else:
    print(z-0.5)