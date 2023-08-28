#!/usr/bin/env python3
""" 8. Complex types - functions """
from typing import Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function make_multiplier
        t takes a float multiplier as argument
 and returns a function that multiplies a float by multiplier."""
    def square(base: float) -> float:
        return base * multiplier
    return square
