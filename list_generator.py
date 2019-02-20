#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 - Assignment 4"""

import random
# Import for logging

def generateList(num_of_time):
    """Generate list

    Args:
        num_of_time (int): The number of times to add a new input to list

    Returns:
        Returns new list

    """
    new_list = []

    some_random = random.randint(3,57)

    for i in range(num_of_time):
        new_list.append(random.randint(1, num_of_time+1))

    return new_list
