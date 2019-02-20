#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 - Assignment 4"""


# Import the timeit module
import timeit
# Import the Timer class defined in the module
from timeit import Timer
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
        list_size_all (list): Max inputs used to generate lists

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
    list_size_all = [500,1000,10000]

    # Set up logger named assignment2 with output level
    my_logger = logging.getLogger('search_compare')
    my_logger.setLevel(logging.WARNING)
    # Add the log message handler to the logger. output to file
    handler = logging.FileHandler('errors.log')
    my_logger.addHandler(handler)


    # Begin asking for input from user
    while True:
        try:
            print "Find the avgerage time for search:"
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
        total_search_time = 0
        count = 1
        # step through each list size inputs
        for list_size in list_size_all:
            print "Starting search {} ({} of {})...".format(
                                             list_size,count,len(list_size_all))
            # Sum up search times
            total_search_time += findTimeAvg(
                              "sequential_search", 100,list_generator.generateList(list_size))
            count += 1

        avg_search_time = total_search_time / len(list_size_all)

        print "\nSequential Search took %10.7f seconds to run, on average\n" % avg_search_time

        main()

    elif user_input == 2:
        total_search_time = 0
        count = 1
        # step through each list size inputs
        for list_size in list_size_all:
            print "Starting search {} ({} of {})...".format(
                                             list_size,count,len(list_size_all))
            # Sum up search times
            total_search_time += findTimeAvg(
              "ordered_sequential_search", 100,sorted(list_generator.generateList(list_size)))
            count += 1

        avg_search_time = total_search_time / len(list_size_all)

        print "\nSequential Search (Ordered) took %10.7f seconds to run, on average\n" % avg_search_time

        main()

    elif user_input == 3:
        total_search_time = 0
        count = 1
        # step through each list size inputs
        for list_size in list_size_all:
            print "Starting search {} ({} of {})...".format(
                                             list_size,count,len(list_size_all))
            # Sum up search times
            total_search_time += findTimeAvg(
              "binary_search_iterative", 100,sorted(list_generator.generateList(list_size)))
            count += 1

        avg_search_time = total_search_time / len(list_size_all)

        print "\nBinary Search (Iterative) took %10.7f seconds to run, on average\n" % avg_search_time

        main()

    elif user_input == 4:
        total_search_time = 0
        count = 1
        # step through each list size inputs
        for list_size in list_size_all:
            print "Starting search {} ({} of {})...".format(
                                             list_size,count,len(list_size_all))
            # Sum up search times
            total_search_time += findTimeAvg(
              "binary_search_recursive", 100,sorted(list_generator.generateList(list_size)))
            count += 1

        avg_search_time = total_search_time / len(list_size_all)

        print "\nBinary Search (Recursive) took %10.7f seconds to run, on average\n" % avg_search_time

        main()

    elif user_input == 5:
        print '\nOk bye.\n'

    else:
        print '\nMake a valid selection\n'
        main()


def findTimeAvg(search_type_name, num_of_list, generated_list):
    """Finds the search time for the given search algo

    Args:
        search_type_name (string): The number of times to add a new input to list
        num_of_list (int): The number of times to run timeit
        generated_list(list): List to search through

    Attributes:
        search_value (int): The search value. Default to -1 for assignment
        timer_string (string): String used by timeit.timer
        timerit_num (int): Number of test runned by timeit
        timeit_total (int): sum of the the timeit

    Return:
        avgerage of total time

    """
    search_value = -1
    timer_string = "{}({}, {})".format(search_type_name, generated_list, search_value)
    timerit_num = 10
    timeit_total = 0

    #print generated_list[0], generated_list[1]

    # preapre timer obj to benchmark search
    t1 = Timer(timer_string, "from __main__ import {}".format(search_type_name))

    # Loop and sum the time it took to execute search
    for i in range (num_of_list):
        timeit_total +=  t1.timeit(number=timerit_num)

    return timeit_total / num_of_list


def sequential_search(a_list, search_item):
    """Sequenial Search Algorithm

    Args:
        a_list(list): List to search through
        search_item (int): The to be searched

    Attributes:
        position (int): The cursor postion of a_list
        found (bool): Search item found

    Return:

    """
    position = 0
    found = False

    while position < len(a_list) and not found:
        if a_list[position] == search_item:
            found = True
        else:
            position += 1

    return found


def ordered_sequential_search(a_list, search_item):
    """Sequenial Search Sequential Algorithm

    Args:
        a_list(list): List to search through
        search_item (int): The to be searched

    Attributes:
        position (int): The cursor postion of a_list
        found (bool): Search item found
        stop (bool): Stop search

    Return:

    """
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

    return found


def binary_search_iterative(a_list, search_item): #assumes sorted list
    """Binary Search Iterative Algorithm. Assumed sorted list

    Args:
        a_list(list): List to search through
        search_item (int): The to be searched

    Attributes:
        first_position (int): The current cursor at top of a_list
        last_position (int): The current cursor at bottom of a_list
        found (bool): Search item found

    Return:

    """
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

    return found


def binary_search_recursive(a_list, search_item):
    """Binary Search Recursive Algorithm. Assumed sorted list

    Args:
        a_list(list): List to search through
        search_item (int): The to be searched

    Attributes:
        midpoint (int): The middle of the list

    Return:

    """
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2

    if a_list[midpoint] == search_item:
        return True
    else:
        if search_item < a_list[midpoint]:  # chop and thow away half
            return binary_search_recursive(a_list[:midpoint], search_item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], search_item)



# Run main if file direcrly executed
if __name__ == '__main__':
    main()
