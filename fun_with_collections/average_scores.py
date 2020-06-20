"""
Program: average_scores.py
Author: Paul Elsea
Last Modified: 06/20/2020

Program to average scores and print arbitrary keywords and values.
"""
from statistics import mean

'''This finds the mean of an arbitrary number of input integers then prints the results. It then prints an
arbitrary number of keywords and their set values, then a whole lot of dashes to make everything look tidy.
:average_score: This is the mean of the input scores
:returns: Nothing. Relevant variables and keywords/values are printed'''
def average_scores(*args, **kwargs):
    average_score = mean(args)
    print(average_score)
    for key, value in kwargs.items():
        print('%s == %s' % (key, value))
    print('-'*50)


if __name__ == '__main__':
    average_scores(80, 89, 92, 96, name='Paul Elsea', course='advanced pencil-whipping', gpa=3.96)
    average_scores(98, 99, 97, name='Billy Bob', course='particle entanglement in subatomic interactions', gpa=3.99)
    average_scores(1, 0, name='Dirk Svenson', lunch='Surströmming', how_much_he_cares='1.2%')
    average_scores(50, 50, 50, 50, 50, name='Suzy TestCase', control_case='yes', gpa='strictly average')
    average_scores(100, 100, 100, 100, 100, species='Cat', name='Vern', shrew_kill_success='100%')