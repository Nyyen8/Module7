"""
Program: sort_and_search_array.py
Author: Paul Elsea
Last Modified: 06/21/2020

Program to sort and search arrays.
"""
import array as arr

'''Function to accept user input.
:user_input: input from user.
:returns: User input'''
def get_input():
    user_input = input('Please enter a number from 0 to 9.\n')
    return user_input

'''Function to accept user input and verify it is a positive whole number from 1 to 9.
:input: User input passed into the function.
:valid_input: Input that has been shows to be an integer
:returns: valid_input'''
def validate_input(user_input):
    while True:
        try:
            valid_input = int(user_input)
            if valid_input > 9:
                print('Number too high. Choose a number from 0 to 9')
                user_input = input()
                continue
            elif valid_input < 0:
                print('Number too low. Choose a number from 0 to 9')
                user_input = input()
                continue
            else:
                break
        except ValueError:
            print('Invalid input. Please use only numbers from 0 to 9')
            user_input = input()
            continue
    return valid_input

'''This declares an array then calls the get_input func from within a for-in
loop to populate it. Results are returned.
:output_array: Array that is returned and is filled with single digit numbers by user.
:array_length: The final length desired of the array.
:returns: Populated array'''
def build_array():
    input_list = []
    array_length = 3

    for index in range(array_length):
        input_list.append(validate_input(get_input()))

    output_array = arr.array('i', input_list)
    return output_array

'''This returns a sorted version of an input array.
:returns: sorted input_array'''
def sort_array(input_array):
    sorted_array = arr.array('i', sorted(arr.array.tolist(input_array)))
    return sorted_array
    '''This function uses "return" as it uses the sorted() func which doesn't modify the 
    original array, instead returning a new sorted instance. Without the return here 
    you would have to add the print func into the function, making it do double duty. It also 
    lets you pass the returned list into other code so it aids in modularity.'''

'''This returns the index of a search variable from the input array.
:search_item: This is the string to be searched for in the array.
:returns: Index of search item, or "-1" if string is not present in the array.'''
def search_array(searched_array, search_item):
    try:
        return searched_array.index(search_item)
    except ValueError:
        return -1

if __name__ == '__main__':
    new_array = build_array()
    print(search_array(new_array, 3))
    print(sort_array(new_array))