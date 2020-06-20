"""
Program: basic_list.py
Author: Paul Elsea
Last Modified: 06/19/2020

Program to accept user input to populate a list.
"""

'''This declares a list variable then calls the get_input func from within a for-in
loop to populate it. Results are returned.
:output_list: List that is returned and is filled with single digit numbers by user.
:list_length: The final length desired of the list.
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

'''Function to accept user input and verify it is a positive whole number from 1 to 9.
:input: User input passed into the function.
:valid_input: Input that has been shows to be an integer
:returns: Nothing'''
def validate_input(input):
        try:
            valid_input = int(input)
            if valid_input > 50:
                # print('Number too high. Choose a number from 1 to 50')
                # continue
                raise ValueError
            elif valid_input < 1:
                # print('Number too low. Choose a number from 1 to 50')
                # continue
                raise ValueError
            else:
                return valid_input
        except ValueError:
            # print('Invalid input. Please use only numbers from 1 to 50')
            # continue
            raise ValueError

if __name__ == '__main__':
    print(make_list())