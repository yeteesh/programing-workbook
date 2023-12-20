'''
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a b
##Hint: You will probably find the log10 function in the math module helpful
for computing the second last item in the list
'''
print(' Pick one number')
x = int(input())
print ('Pick another number')
y = int(input())
import math 
print(x+y)
print(y-x)
print(x*y)
print(x/y)
print(x%y)
print(math.log10(x))
print(math.log10(y))