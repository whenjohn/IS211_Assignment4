#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 - Assignment 4"""

# Import the time module
import time
# Import random number generator
import random
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
        >>> $ python search_compare.py
        Find the avgerage time for search:
        1 - Sequential Search
        2 - Sequential Search (Ordered)
        3 - Binary Search (Iterative)
        4 - Binary Search (Recursive)
        5 - Quit
        Please enter 1 - 5:
        Binary Search (Recursive) took  0.0004027 seconds to run, on average
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
            print "Find the average search time for worst case:"
            print "1 - Sequential Search"
            print "2 - Sequential Search (Ordered)"
            print "3 - Binary Search (Iterative)"
            print "4 - Binary Search (Recursive)"
            print "5 - Quit"
            user_input = int(input("Please enter 1 - 5: "))
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
                func_return = sequential_search(list_generator.generateList(element_size,3), -1)
                #print func_return
                total_time += func_return[1]
            avg_time = total_time / num_of_lists
            print "Sequential Search for",element_size,"elements took%10.7f seconds to run, on average" % avg_time
        print "\n"
        main()

    elif user_input == 2:
        total_time = 0
        # step through each list size inputs
        print "\n"
        for element_size in element_size_all:
            for i in range (num_of_lists):
                func_return = ordered_sequential_search(list_generator.generateList(element_size,1), -1)
                #print func_return
                total_time += func_return[1]
            avg_time = total_time / num_of_lists
            print "Sequential Search (Ordered) for",element_size,"elements took%10.7f seconds to run, on average" % avg_time
        print "\n"
        main()


    elif user_input == 3:
        total_time = 0
        # step through each list size inputs
        print "\n"
        for element_size in element_size_all:
            for i in range (num_of_lists):
                func_return = binary_search_iterative(list_generator.generateList(element_size,1), -1)
                #print func_return
                total_time += func_return[1]
            avg_time = total_time / num_of_lists
            print "Binary Search (Iterative) for",element_size,"elements took%10.7f seconds to run, on average" % avg_time
        print "\n"
        main()

    elif user_input == 4:
        total_time = 0
        # step through each list size inputs
        print "\n"
        for element_size in element_size_all:
            for i in range (num_of_lists):
                func_return = binary_search_recursive(list_generator.generateList(element_size,1), -1)
                #print func_return
                total_time += func_return[1]
            avg_time = total_time / num_of_lists
            print "Binary Search (Recursive) for",element_size,"elements took%10.7f seconds to run, on average" % avg_time
        print "\n"
        main()

    elif user_input == 5:
        print '\nOk bye.\n'

    else:
        print '\nMake a valid selection\n'
        main()


def sequential_search(a_list, search_item):
    """Sequenial Search Algorithm

    Args:
        a_list(list): List to search through
        search_item (int): The to be searched
        start & finish (time): start and stop time of the function

    Attributes:
        position (int): The cursor postion of a_list
        found (bool): Search item found

    Return:

    """
    start = time.time()
    position = 0
    found = False

    while position < len(a_list) and not found:
        if a_list[position] == search_item:
            found = True
        else:
            position += 1

    finish = time.time()
    return found, finish-start


def ordered_sequential_search(a_list, search_item):
    """Sequenial Search Sequential Algorithm

    Args:
        a_list(list): List to search through
        search_item (int): The to be searched
        start & finish (time): start and stop time of the function

    Attributes:
        position (int): The cursor postion of a_list
        found (bool): Search item found
        stop (bool): Stop search

    Return:

    """
    start = time.time()
    position = 0
    found = False
    stop = False

    while position < len(a_list) and not found and not stop:
        if a_list[position] == search_item:
            found = True
        else:
            if a_list[position] > search_item:
                stop = True
            else:
                position += 1

    finish = time.time()
    return found, finish-start


def binary_search_iterative(a_list, search_item): #assumes sorted list
    """Binary Search Iterative Algorithm. Assumed sorted list

    Args:
        a_list(list): List to search through
        search_item (int): The to be searched
        start & finish (time): start and stop time of the function

    Attributes:
        first_position (int): The current cursor at top of a_list
        last_position (int): The current cursor at bottom of a_list
        found (bool): Search item found

    Return:

    """
    start = time.time()
    first_position = 0
    last_position = len(a_list) - 1
    found = False

    while first_position <= last_position and not found:
        midpoint = (first_position + last_position) // 2

        if a_list[midpoint] == search_item:
            found = True
        else:
            if search_item < a_list[midpoint]:
                last_position = midpoint - 1
            else:
                first_position = midpoint + 1

    finish = time.time()
    return found, finish-start


def binary_search_recursive(a_list, search_item):
    """Binary Search Recursive Algorithm. Assumed sorted list

    Args:
        a_list(list): List to search through
        search_item (int): The to be searched
        start & finish (time): start and stop time of the function

    Attributes:
        midpoint (int): The middle of the list

    Return:

    """
    start = time.time()
    if len(a_list) == 0:
        finish = time.time()
        return False, finish-start
    else:
        midpoint = len(a_list) // 2

    if a_list[midpoint] == search_item:
        finish = time.time()
        return True, finish-start
    else:
        if search_item < a_list[midpoint]:  # chop and thow away half
            return binary_search_recursive(a_list[:midpoint], search_item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], search_item)



# Run main if file direcrly executed
if __name__ == '__main__':
    main()
