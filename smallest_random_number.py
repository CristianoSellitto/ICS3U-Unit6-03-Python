#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in December 2022
# A program that finds the smallest number from a list of ten random numbers

import random


def find_smallest_number_array(number_array):
    # Finds the smallest number from a list of ten random numbers

    smallest_number = number_array[0]

    for number in number_array:
        if number < smallest_number:
            smallest_number = number

    return smallest_number


def main():
    # Generates ten random numbers in an array and calls a function

    random_array = []

    for counter in range(0, 10):
        random_number = random.randint(0, 100)
        random_array.append(random_number)
        print("Random #{0} is {1}".format(counter + 1, random_number))
    smallest_number_array = find_smallest_number_array(random_array)
    print("\nThe smallest number in this array is {}.".format(smallest_number_array))

    print("\nDone.")


if __name__ == "__main__":
    main()
