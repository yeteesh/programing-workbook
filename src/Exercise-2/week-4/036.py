## Name That Shape
'''Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.'''
print('Enter the amount of sides in your shape (the limit is 8 sides and you can not have 2 sides):')
s = int(input())
if s == 1:
    print('circle')
if s == 3:
    print('Triangle')
if s == 4:
    print('Square')
if s == 5:
    print('Pentagon')
if s == 6:
    print('Hexagon')
if s == 7:
    print('Heptagon')
if s == 8:
    print('Octagon')