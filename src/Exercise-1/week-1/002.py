## Area of a Field
'''
Create a program that reads the length and width of a farmer’s field from the user ind
feet. Display the area of the field in acres.
## Hint: There are 43,560 square feet in an acre.
'''
print('What is the width of your field in feet')
w = int(input())
print('What is the length of your field in feet')
l = int(input())
print ( (w*l) / 43560 )