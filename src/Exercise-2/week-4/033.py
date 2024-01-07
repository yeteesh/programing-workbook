## Even or Odd?
'''Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.'''
print('Enter a integer:')
i = int(input())
if( i % 2) == 0:
    print("number is even")
else:
    print("number is odd")