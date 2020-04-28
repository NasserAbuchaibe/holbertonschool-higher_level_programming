#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number1 = number * (-1)
    mod1 = number1 % 10
else:
    mod1 = number % 10
if mod1 > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, mod1))
elif mod1 == 0:
    print("Last digit of {} is {} and is 0".format(number, mod1))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, mod1))




