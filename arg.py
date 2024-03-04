#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("square", help="display a square of a given number", type=int)
parser.add_argument("age", help="Please enter your", type=int)
args = parser.parse_args()

#if args.age > 50:
#  print("you are above 50")
#elif args.age < 50:
#  print("you are below 50")
#else:
# print("you are equal to 50")
if args.age <= -1:
  print("DANGER.....")
else:
  print("seems you didn't enter the correct input Eg: value shoube be -1 or less than that")
