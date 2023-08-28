#!/usr/bin/env python3
""" 9. Let's duck type an iterable object """
from typing import Union, Tuple, Callable, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
