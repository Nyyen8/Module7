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
        output_list.append(get_input())

    return output_list

'''Function to accept user input, verify it is a positive whole number from 1 to 9.
:user_input: The integer to be returned.
:returns: Validated integer from 1 to 9'''
def get_input():
    while True:
        try:
            user_input = int(input('Please enter a number from 1 to 9.\n'))
            if user_input > 9:
                print('Number too high. Choose a number from 1 to 9')
                continue
            elif user_input < 1:
                print('Number too low. Choose a number from 1 to 9')
                continue
            else:
                break
        except ValueError:
            print('Invalid input. Please use only numbers from 1 to 9')
            continue

    return user_input

if __name__ == '__main__':
    print(make_list())