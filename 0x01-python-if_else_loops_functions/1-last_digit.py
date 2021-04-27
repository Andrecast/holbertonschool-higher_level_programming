#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    if number % 10 > 5:
        print("Last digit of {} is {} and\
 is greater than 5".format(number, number % 10))
    elif number % 10 == 0:
        print("Last digit of {} is {} and\
 is 0".format(number, number % 10))
    elif (number % 10) < 6 and (number % 10) != 0:
        print("Last digit of {} is {} and\
 is less than 6 and not 0".format(number, number % 10))
else:
    n = -number  # lo vuelvo positivo para que me calcule el módulo que quiero
    # el modulo de un numero negativo es diferente
    if n % 10 == 0:
        print("Last digit of {} is {} and\
 is 0".format(number, -(n % 10)))
    elif (n % 10) < 6 and (n % 10) != 0:
        print("Last digit of {} is {} and\
 is less than 6 and not 0".format(number, -(n % 10)))
