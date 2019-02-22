#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 - Assignment 4"""

import random


def generateList(num_of_elements, case_scenario):
    """Generate list

    Args:
        num_of_time (int): The number of times to add a new input to list
        case_scenario (int): Best (1) - sorted list, avg (2) - half sort, worst (3) - no sort case scenerio

    Returns:
        Returns new list

    """
    list_full = []
    half_num_of_elements = num_of_elements / 2

    list_full = range(num_of_elements)

    list_first_half = list_full[:(half_num_of_elements)]
    list_second_half = list_full[(half_num_of_elements):]

    if case_scenario == 1:
        return list_full
    if case_scenario == 2:
        random.shuffle(list_second_half)
        return list_first_half + list_second_half
    if case_scenario == 3:
        random.shuffle(list_full)
        return list_full
