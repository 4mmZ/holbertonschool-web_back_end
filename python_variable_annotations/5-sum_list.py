#!/usr/bin/env python3
""" 5. Complex types - list of floats """
from typing import List


def sum_list(imputlist: List[float]) -> float:
    """ type-annotated function sum_list which takes a list input_list
     of floats as argument and returns their sum as a float. """

    result = 0.0

    for index in imputlist:
        result += index
    return result
