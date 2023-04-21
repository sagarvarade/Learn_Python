import math
from math import sqrt

import sys 

import argparse


print(math.sqrt(4))
print(sqrt(49))

# Read from prompt
a=input("Enter value for  a: ")
print("Value of a : ",a)

# Reading from prompt as String[] args main from java
print(sys.argv)
for x in sys.argv:
    print(x)


parser=argparse.ArgumentParser(
    description="This program print the name of my dogs"
)

parser.add_argument('-c','--color',metavar='color',required=True,help='The color to search for')
args=parser.parse_args()
print(args.color)