"""
Program: file_IO.py
Author: Paul Elsea
Last Modified: 06/20/2020

Program to read from and write to a file.
"""
import os as os

'''This opens student_info.txt in append mode, then writes the input tuple into the file.
:write_doc: The file being opened.
:input_info: The input tuple to be written.
:returns: Nothing.'''
def write_to_file(input_info):
    with open('student_info.txt', 'a') as write_doc:
        write_doc.write(str(input_info)+'\n')
    write_doc.close()

'''This accepts user input of student name, number of scores, then scores themselves, writes it to a list, then
converts the list to a tuple and passes it to write_to_file().
:student_info: List to be populated by user input.
:count: counter variable
:score_num: Int variable to set to determine how many scores are needed.
:finalized_student_info: Finished populated list that is then converted to a tuple.
:returns: Nothing.'''
def get_student_info():
    student_info = []
    student_info.append(input('Please enter student name:\n'))
    count = 0
    score_num = int(input('Please enter number of scores to be entered:\n'))
    while count < score_num:
        student_info.append(input('Please enter score:\n'))
        count += 1
    finalized_student_info = tuple(student_info)
    write_to_file(finalized_student_info)

'''Opens work file and reads contents.
:file_name: The file to be read
:read_file: The object being used to read from the file
:line: The individual line being pulled from the file.
:returns: Nothing.'''
def read_from_file():
    file_dir = os.path.dirname(__file__)
    file_name = 'student_info.txt'
    read_file = open(os.path.join(file_dir, file_name), 'r')
    line = read_file.read()
    print(line)
    read_file.close()

if __name__ == '__main__':
    get_student_info()
    get_student_info()
    get_student_info()
    get_student_info()

    read_from_file()
    input('Press enter to quit.')