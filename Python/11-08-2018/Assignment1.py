# Assignemt1- Problem 2

'''
Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
in a comma-separated sequence on a single line.
'''


def factor_7():
    return [n for n in range(2000, 3201) if n % 7 == 0 and n % 5 != 0]


# print(factor_7())

# ****************************************************************** #
# ****************************************************************** #
# ****************************************************************** #

# Assignemt1- Problem 3

'''
Write a Python program to accept the user's first and last name and then getting them printed
in the the reverse order with a space between first name and last name.
'''


def reverse_name(fname, lname):
    full_name = fname + ' ' + lname
    return full_name[::-1]


# print(reverse_name('Manish', 'Agrawal'))

# ****************************************************************** #
# ****************************************************************** #
# ****************************************************************** #

# Assignemt1- Problem 4

'''
Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r3
'''

import math


def sphere_volume(r):
    return round((4 / 3) * math.pi * (r ** 3), 2)


print(sphere_volume(12))
