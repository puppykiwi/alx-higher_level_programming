#!/usr/bin/python3
import random
number = random.randint(-10, 10)
val = number % 10

if val > 5:
    print("Last digit of", number, "is", val, "and is greater than 5")
elif val == 0:
    print("Last digit of", number, "is", val, "and is 0")
elif val < 6 and val != 0:
    print("Last digit of", number, "is", val, "and is less than 6 and not 0")
