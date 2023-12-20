## Making Change
'''Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.
##Hint: A one dollar coin was introduced in Canada in 1987. It is referred to as a loonie
because one side of the coin has a loon (a type of bird) on it. The two dollar
coin, referred to as a toonie, was introduced 9 years later. It’s name is derived
from the combination of the number two and the name of the loonie.
'''
print('Welcome to Costco you are at the self checkout section')
print('Enter the item you are purchasing and place it aluminum table of your right')
x = input('')
print('Enter 2 if you confirm or enter 1 ')
v = int(input())
print('If you entered 2 on the previous step then enter number 1 and if you entered 1 on the previous step then enter 2 now ')
w = int(input())
print('Enter the price of your item')
a = int(input())
print('Enter the amount of cash you will be paying')
z = int(input()) 
print('Place the cash in the dispenser below')
if z > a:
    print(z-a('is your change'))
print('your cash will be placed in the dispenser')
  
