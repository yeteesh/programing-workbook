## Day Old Bread
'''A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. Each of
these amounts should be displayed on its own line with an appropriate label. All of
the values should be displayed using two decimal places, and the decimal points in
all of the numbers should be aligned when reasonable values are entered by the user.'''

print('Enter the number of loaves of day old bread you purchased:')
d = int(input())
print('Enter the number of regular bread you purchased:')
r = int(input())
print('The amount of money you have to pay for the regular bread is beleow')
print(r*3.49)
print('The amount of money you have to pay for the day old bread is beleow')
print((d*3.49)*0.60)
print('The total cost for today is beleow')
print((r*3.49)+((d*3.49)*0.60))
