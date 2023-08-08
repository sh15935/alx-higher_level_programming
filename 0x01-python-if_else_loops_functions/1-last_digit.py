#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dight = abs(number)%10
if last_dight > 5:
    print(f"Last digit of {number} is {last_dight} and is greater than 5")
elif last_dight == 0:
    print(f"Last digit of {number} is {last_dight} and is 0")
else:
    print(f"Last digit of {number} is {last_dight} and is less than 6 and not 0\n")
