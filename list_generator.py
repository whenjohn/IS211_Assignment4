#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 - Assignment 4"""

import random
# Import for logging

def generateList(num_of_elements, case_scenario):
    """Generate list

    Args:
        num_of_time (int): The number of times to add a new input to list
        case_scenario (int): Best (1) - sorted list, avg (2) - half sort, worst (3) - no sort case scenerio
    Returns:
        Returns new list

    """
    new_list1 = []
    new_list2 = []
    half_num_of_elements = num_of_elements / 2

    some_random = random.randint(3,57)

    for i in range(half_num_of_elements):
            new_list1.append(random.randint(1, num_of_elements+1))
            new_list2.append(random.randint(1, num_of_elements+1))

    if case_scenario == 1:
        return sorted(new_list1 + new_list2)
    if case_scenario == 2:
        return sorted(new_list1) + new_list2
    if case_scenario == 3:
        return new_list1 + new_list2
