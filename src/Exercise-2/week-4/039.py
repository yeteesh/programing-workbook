# Classifying Triangles
'''A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
scalene. All three sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of the three sides of a triangle from the
user. Then display a message that states the triangle’s type.'''
print('Enter the lengths of your triangle:')
x = int(input())
y = int(input())
z = int(input())
if x == y == z:
    print('Equilaterall')
if x == y != z or x != y == z:
    print('Isosceles')
if x != y != z:
    print('Scalene')
