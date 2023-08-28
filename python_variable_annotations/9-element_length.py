#!/usr/bin/env python3
""" 9. Let's duck type an iterable object """
from typing import Union, Tuple, Callable, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    " Function that takes a list as input and returns a list of tuples."
    return [(i, len(i)) for i in lst]
