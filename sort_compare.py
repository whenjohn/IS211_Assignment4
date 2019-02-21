#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 - Assignment 4"""


# Import the time module
import time
# Import for logging
import logging
import logging.handlers
# Import custom function to generate lists
import list_generator



def main():
    """Main function that runs at start of program.

    Attributes:
        element_size_all (list): Max elements of a list
        num_of_lists (int): The number of lists per search function

    Returns:
        User promted to enters info. Program will perform action and return
            results
        Outputs to error.log file

    Examples:
        >>> $ python sort_compare.py
        Find the avgerage time for sort:
        1 - Insertion Sort
        2 - Shell Sort
        3 - Python Sort
        4 - Quit
        Please enter 1 - 4:
        Python Sort took  0.0011004 seconds to run, on average
    """
    element_size_all = [500,1000,10000]
    num_of_lists = 100

    # Set up logger named assignment2 with output level
    my_logger = logging.getLogger('search_compare')
    my_logger.setLevel(logging.WARNING)
    # Add the log message handler to the logger. output to file
    handler = logging.FileHandler('errors.log')
    my_logger.addHandler(handler)


    # Begin asking for input from user
    while True:
        try:
            print "Find the average sort time:"
            print "1 - Insertion Sort"
            print "2 - Shell Sort"
            print "3 - Python Sort"
            print "4 - Quit"
            user_input = int(input("Please enter 1 - 4: "))
        except (SyntaxError, NameError) as exception:
            # what about floats?
            my_logger.error('Error: Input is incorrect. {}'.format(
                                                            exception.message))
            print('\nYou have not entered a number.\n')
            continue
        else:
            # int num entered. break loop and continue
            break

    # Process selection and calculate results
    if user_input == 1:
        total_time = 0
        # step through each list size inputs
        print "\n"
        for element_size in element_size_all:
            for i in range (num_of_lists):
                func_return = insertion_sort(list_generator.generateList(element_size,2))
                total_time += func_return[1]
            avg_time = total_time / num_of_lists
            print "Insertion Sort for",element_size,"elements took%10.7f seconds to run, on average" % avg_time
        print "\n"
        main()

    elif user_input == 2:
        total_time = 0
        # step through each list size inputs
        print "\n"
        for element_size in element_size_all:
            for i in range (num_of_lists):
                func_return = shell_sort(list_generator.generateList(element_size,2))
                total_time += func_return[1]
            avg_time = total_time / num_of_lists
            print "Shell Sort for",element_size,"elements took%10.7f seconds to run, on average" % avg_time
        print "\n"
        main()

    elif user_input == 3:
        total_time = 0
        # step through each list size inputs
        print "\n"
        for element_size in element_size_all:
            for i in range (num_of_lists):
                func_return = python_sort(list_generator.generateList(element_size,2))
                total_time += func_return[1]
            avg_time = total_time / num_of_lists
            print "Python Sort for",element_size,"elements took%10.7f seconds to run, on average" % avg_time
        print "\n"
        main()

    elif user_input == 0:
        total_sort_time = 0
        count = 1
        # step through each list size inputs
        for element_size in element_size_all:
            print "SECRET"

            usorted = list_generator.generateList(element_size)

            print "Unsorted: {}\n\n".format(usorted)
            print "Sorted: {}\n\n".format(python_sort(
                                        list_generator.generateList(element_size,2)))
            count += 1
        main()

    elif user_input == 4:
        print '\nOk bye.\n'

    else:
        print '\nMake a valid selection\n'
        main()


def insertion_sort(a_list):
    """Insertion Sort Algorithm.

    Args:
        a_list(list): List to search through

    Attributes:
        current_value (int): Container for selected postion. Move down line.
        postion (int): Cursor position in list
        start & finish (time): start and stop time of the function

    Return:
        a_list(list): sorted list

    """
    start = time.time()
    for index in range(1, len(a_list)):
    	current_value = a_list[index]
    	position = index
        # step back to begining and compare
    	while position > 0 and a_list[position - 1] > current_value:
    		a_list[position] = a_list[position - 1] # shift larger value(s) forward
    		position = position - 1 # step cursor back

    	a_list[position] = current_value # when find a place for value

    finish = time.time()
    return a_list, finish-start


def shell_sort(a_list):
    """Shell Sort Algorithm.

    Args:
        a_list(list): List to search through

    Attributes:
        sublist_count (int): Split list in half
        start & finish (time): start and stop time of the function

    Return:
        a_list(list): sorted list

    """
    start = time.time()
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
    	for start_position in range(sublist_count):
    		gap_insertion_sort(a_list, start_position, sublist_count)

    	# Goes through a few incement aka gap size.
        # Each time apply gap_insertion_sort logic
    	sublist_count = sublist_count // 2

    finish = time.time()
    return a_list, finish-start

def gap_insertion_sort(a_list, start, gap):
    """Part of Shell Sort Algorithm. This is the insertion portion

    Args:
        a_list(list): List to search through
        start(int): the start position
        gap(int): the size of the space between the search values

    Attributes:
        current_value (int): Current value at current cursor
        position (int): the incriement

    Return:
        a_list(list): sorted list

    """
    for i in range(start + gap, len(a_list), gap):
         # like the temp in bubble.
         # holds the value that is moved down while other vales shift up
    	current_value = a_list[i]
    	position = i

    	# logic for insertion sort
        # checks back and shift larger values forward
    	while position >= gap and a_list[position - gap] > current_value:
    		a_list[position] = a_list[position - gap]
    		position = position - gap

    	a_list[position] = current_value


def python_sort(a_list):
    """Python build-in sort function

    Args:
        a_list(list): List to search through
        start & finish (time): start and stop time of the function

    Return:
        a_list(list): sorted list

    """
    start = time.time()
    finish = time.time()
    return sorted(a_list), finish-start


# Run main if file direcrly executed
if __name__ == '__main__':
    main()
