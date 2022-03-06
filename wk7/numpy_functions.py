# Ishai Masada
# NumPy Functions
import numpy as np
import random

def one_dim(list_of_num_values):
    return np.array(list_of_num_values)

def append_to(num_array, new_element):
    # append to the array
    return np.append(num_array, new_element)

def rep_negative(num_array):
    # replace all of the negative numbers with a 0
    return np.where(num_array < 0, 0, num_array)

def find_comm(num_array_one, num_array_two):
    # find all of the common elements
    print(f'array one: {num_array_one}')
    print(f'array two: {num_array_two}')
    return np.intersect1d(num_array_one, num_array_two)

def main():
    num_values = [1, 2, 3, 4, 5, -6, -2, -9, -1]
    original_array = one_dim(num_values)
    print(f'One dimensional array: {original_array}')

    # Appending elements to the array
    new_element = int(input('Type in an integer to add to the array: '))
    appended_array = np.array(list(map(int, append_to(original_array, new_element))))
    print(f'Appended array: {appended_array}')

    # Replacing all of the negative values with zeros
    print(f'Changed array: {rep_negative(original_array)}')

    # Finding the common numbers
    num_array_one = one_dim([num for num in range(random.randrange(1, 20))])
    num_array_two = one_dim([num for num in range(random.randrange(1, 20))])
    print(f'Common numbers between array one and array two: {find_comm(num_array_one, num_array_two)}')

main()
