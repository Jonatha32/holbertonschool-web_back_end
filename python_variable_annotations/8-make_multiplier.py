#!/usr/bin/env python3
"""
 a type-annotated function sum_mixed_list which takes a list mxd_lst
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """"Returns a function that multiplies a float by multiplier"""
    def multiply_function(x: float) -> float:
        return x * multiplier
    return multiply_function
