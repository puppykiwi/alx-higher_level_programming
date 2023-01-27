#!/usr/bin/python3
import sys

num = len(sys.argv)
if num == 1:
    print("0 arguments.")
elif num == 2:
    print("1 argument:", end='\n')
elif num > 2:
    print("{} arguments:".format(num), end='\n')

for i in range(1, num):
    print("{:d}:".format(i), sys.argv[i])
