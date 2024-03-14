#!/usr/bin/env python3

"""
Annotating a given function
"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    a func that returns values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
