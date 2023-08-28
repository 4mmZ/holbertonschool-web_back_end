#!/usr/bin/env python3
""" 6. Complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ type-annotated function sum_mixed_list which takes a list
      mxd_lst of integers and floats and returns their sum as a float. """

    result = 0.0

    for index in mxd_lst:
        result += index
    return result
