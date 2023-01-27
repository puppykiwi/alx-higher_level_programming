#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
val = abs(number) % 10
string = "and is less than 6 and not 0"
if number >= 0:
    if val > 5:
        print("Last digit of", number, "is", val, "and is greater than 5")
    elif val == 0:
        print("Last digit of", number, "is", val, "and is 0")
    elif val < 6 and val != 0:
        print("Last digit of", number, "is", val, string)

if number < 0:
    if val == 0:
        print("Last digit of", number, "is", val, "and is 0")
    if val != 0:
        print("Last digit of", number, "is", val * -1, string)
