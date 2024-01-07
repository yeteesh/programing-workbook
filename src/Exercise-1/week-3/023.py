# Units of Time (Again)
'''In this exercise you will reverse the process described in Exercise 24. Develop a
program that begins by reading a number of seconds from the user. Then your program
should display the equivalent amount of time in the form D:HH:MM:SS, where D,
HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours,
minutes and seconds should all be formatted so that they occupy exactly two digits.
Use your research skills determine what additional character needs to be included in
the format specifier so that leading zeros are used instead of leading spaces when a
number is formatted to a particular width.'''
import time
print('Enter the amount of seconds:')
s = int(input())
print(s/86400)
print('The first number is seconds into days')
print(s/3600)
print('The second number is seconds into hours')
print(s/60)
print('The third number is seconds into minutes ')
print(s/1)
print('The fourth number is seconds into seconds')