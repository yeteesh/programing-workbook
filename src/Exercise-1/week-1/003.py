## Bottle Deposits
'''
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and two digits to the right of the decimal point.
'''
# 1 = less than 1 liter  2 = more than or equal to 1 liter 
print ('Enter size of bottle,1 = less than 1 liter or equal to 1 liter  2 = more than 1 liter: ')
x = int(input())
print('Are you sure, if you entered a number 2 then enter number less than 2 and if you entered number 1 then enter a number less than 1:')
y = int(input())
if x > y:
    print (' You will receive $0.10 in your bank account')
if x < y:
    print('You will receive $0.25 in your bank account')