# Vowel or Cons
'''In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.'''
print('Enter a letter in the alphabet:')
a = str(input())
# vowels = ['a','e','i','o','u']
# print(vowels.index(a))
if ['a','e','i','o','u'].index(a) >= 0:
    print('Your letter had a vowel in it.')
else:
    print('your letter did not have any vowls in it.')
    