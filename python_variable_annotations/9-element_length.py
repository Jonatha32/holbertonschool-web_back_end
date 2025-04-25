#!/usr/bin/env python3
"""
 Annotate the below function parameters and return values with appropriate type
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing elements"""
    return [(i, len(i)) for i in lst]
