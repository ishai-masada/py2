#####################################################################################
#
# Name:   Ishai Masada
#
# Date:   3/9/22
#
# Purpose:  Implement NumPy functions
#
# Functions:       one_dim, append_to, rep_negative, find_comm, main
#
# Update:   None
#
#####################################################################################


import numpy as np
import random

#####################################################################################
#
# Function Name:  one_dim
#
# Date:           3/9/22
#
# Purpose:       Create a one-dimensional array from a list of numbers
#
# Who called:           main function
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def one_dim(list_of_num_values):
    return np.array(list_of_num_values)

#####################################################################################
#
# Function Name:  append_to
#
# Date:           3/9/22
#
# Purpose:       Appends an element to an array
#
# Who called:           main function
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def append_to(num_array, new_element):
    return np.append(num_array, new_element)

#####################################################################################
#
# Function Name:  rep_negative
#
# Date:           3/9/22
#
# Purpose:       Replaces all of the negative values in the array with a 0
#
# Who called:           main function
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def rep_negative(num_array):
    return np.where(num_array < 0, 0, num_array)

#####################################################################################
#
# Function Name:  find_comm
#
# Date:           3/9/22
#
# Purpose:       Finds all of the common elements between two arrays
#
# Who called:           main function
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def find_comm(num_array_one, num_array_two):
    print(f'\nArray one: {num_array_one}')
    print(f'Array two: {num_array_two}')
    return np.intersect1d(num_array_one, num_array_two)

#####################################################################################
#
# Function Name:  main
#
# Date:           3/9/22
#
# Purpose:       Call all of the functions that will be used in the program
#
# Who called:           None
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def main():
    # Creating a one-dimensional array
    num_values = [1, 2, 3, 4, 5, -6, -2, -9, -1]
    original_array = one_dim(num_values)
    print(f'Original List: {num_values}')
    print(f'One dimensional array: {original_array}')

    # Appending elements to the array
    new_element = int(input('\nType in an integer to add to the array: '))
    appended_array = np.array(list(map(int, append_to(original_array, new_element))))
    print(f'\nAppended array: {appended_array}')

    # Replacing all of the negative values with zeros
    print(f'\nArray with all of the negative values replaced with 0: {rep_negative(appended_array)}')

    # Finding the common numbers
    num_array_one = one_dim([num for num in range(random.randrange(1, 20))])
    num_array_two = one_dim([num for num in range(random.randrange(1, 20))])
    print(f'Common numbers between array one and array two: {find_comm(num_array_one, num_array_two)}')

main()
