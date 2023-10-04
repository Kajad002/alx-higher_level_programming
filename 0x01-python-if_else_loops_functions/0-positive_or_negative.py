#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if(number > 0):
    print(number, end=" ")
    print('is positive')
elif(number == 0):
    print(number, end=" ")
    print('is zero')
else:
    print(number, end=" ")
    print('is negative')
