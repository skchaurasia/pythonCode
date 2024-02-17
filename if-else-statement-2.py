#!/usr/bin/python3
Age=input('Enter your age: ')
try:
  if int(Age) >35:
    print('your age is greater than 35')
  elif int(Age) < 35:
    print('your age is less than 35')
  elif int(Age) == 35:
    print('your age is equal to 35')
except ValueError:
   print('you did not enter a number ?')
