#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number[-1] > 5 :
    print('Last digit of', end=" ")
    print(number, end=" ")
    print("is", number[-1], end=" ")
    print("and is greater than 5")
elif number[-1] == 0:
    print('Last digit of', end=" ")
    print(number, end=" ")
    print("is", number[-1], end=" ")
    print("and is 0")
elif number[-1] < 6 and number[-1] != 0:
    print('Last digit of', end=" ")
    print(number, end=" ")
    print("is", number[-1], end=" ")
    print("and is less than 6 and not 0")
