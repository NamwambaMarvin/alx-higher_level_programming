#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
	last = number % 10
if number < 0:
	last = ((number * -1) % 10) * -1
if last > 5:
    string = "Last digit of {0} is {1} and is greater than 5"
elif last == 0:
    string = "Last digit of {0} is {1} and is 0"
elif last < 6 and last != 0:
    string = "Last digit of {0} is {1} and is less than 6 and not 0"
print(string.format(number, last))
