## Height Units
'''Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
##Hint: One foot is 12 inches. One inch is 2.54 centimeters.'''
print('Enter your height in feet')
x = int(input())
print('Enter your height in inches')
y = int(input())
print((x*12+y)*2.54)