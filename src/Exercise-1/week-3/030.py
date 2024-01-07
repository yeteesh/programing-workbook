## Sum of the Digits in an Integer
'''Develop a program that reads a four-digit integer from the user and displays the sum
of its digits. For example, if the user enters 3141 then your program should display
3 + 1 + 4 + 1 = 9.'''

import math
print("Enter any four digit number")
ri = int(input())
if len(ri) == 4 and ri.isnumeric() == True:
    print(ri[0]+ri[1]+ri[2]+ri[3])
else:
    print("Error: should be four digits!")

