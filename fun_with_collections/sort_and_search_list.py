"""
Program: sort_and_search_list.py
Author: Paul Elsea
Last Modified: 06/20/2020

Program to sort and search lists.
"""
ANIMAL_LIST = ['dog', 'cat', 'mouse']

'''This returns a sorted version of the ANIMAL_LIST.
:returns: sorted ANIMAL_LIST'''
def sort_list():
    return sorted(ANIMAL_LIST)
    '''This function uses "return" as it uses the sorted() func which doesn't sort the 
    original list, instead returning a different, modified version. Without the return here 
    you would have to add the print func into the function, making it do double duty. It also 
    lets you pass the returned list into other code so it aids in modularity.'''

'''This returns the index of a search variable from the ANIMAL_LIST.
:searh_item: This is the string to be searched for in the list
:returns: Index of search item, or "-1" if string is not present in the list.'''
def search_list(search_item):
    try:
        return ANIMAL_LIST.index(search_item)
    except ValueError:
        return -1


if __name__ == '__main__':
   print(sort_list())

   print(search_list('cat'))
   print(search_list('whale'))