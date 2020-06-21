"""
Program: sort_and_search_array.py
Author: Paul Elsea
Last Modified: 06/21/2020

Program to sort and search arrays.
"""
import array as ar

'''Function to accept user input.
:user_input: input from user.
:returns: User input'''
def get_input():
    user_input = input('Please enter a number from 1 to 9.\n')
    return user_input

'''Function to accept user input and verify it is a positive whole number from 1 to 9.
:input: User input passed into the function.
:valid_input: Input that has been shows to be an integer
:returns: valid_input'''
def validate_input(input):
    while True:
        try:
            valid_input = int(input)
            if valid_input > 9:
                print('Number too high. Choose a number from 1 to 9')
                continue
            elif valid_input < 1:
                print('Number too low. Choose a number from 1 to 9')
                continue
            else:
                break
        except ValueError:
            print('Invalid input. Please use only numbers from 1 to 9')
            continue
    return valid_input

'''This declares an array then calls the get_input func from within a for-in
loop to populate it. Results are returned.
:output_array: Array that is returned and is filled with single digit numbers by user.
:array_length: The final length desired of the array.
:returns: Populated array'''
def build_array():
    output_array = []
    array_length = 3

    for index in range(array_length):
        output_array.append(validate_input(get_input()))

    return output_array

'''This returns a sorted version of the ANIMAL_LIST.
:returns: sorted ANIMAL_LIST'''
def sort_list():
    return sorted(ANIMAL_LIST)
    '''This function uses "return" as it uses the sorted() func which doesn't sort the 
    original list, instead returning a different, modified version. Without the return here 
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