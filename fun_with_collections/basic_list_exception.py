"""
Program: basic_list_exception.py
Author: Paul Elsea
Last Modified: 06/20/2020

Program to accept user input to populate a list.
"""

'''This declares a list variable then calls the get_input func from within a for-in
loop to populate it. Returned values are check to see if they fall in acceptable range
and are of the correct type. Results are returned.
:output_list: List that is returned and is filled with single digit numbers by user.
:list_length: The final length desired of the list.
:valid_input: Input that has been shown to be an integer, and which is then checked for range
:returns: Populated list'''
def make_list():
    output_list = []
    list_length = 3

    for index in range(list_length):
        try:
            valid_input = int(get_input())
            if valid_input > 50:
                raise ValueError
            elif valid_input < 1:
                raise ValueError
            else:
                output_list.append(valid_input)
        except ValueError:
            raise ValueError

    return output_list

'''Function to accept user input.
:user_input: input from user.
:returns: User input'''
def get_input():
    user_input = input('Please enter a number from 1 to 50.\n')
    return user_input

if __name__ == '__main__':
    print(make_list())