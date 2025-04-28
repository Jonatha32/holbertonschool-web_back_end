#!/usr/bin/env python3
""""
The coroutine will collect 10 random numbers using an async comprehensing
"""

from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """"
    The coroutine will collect 10 random numbers using an async comprehensing
    """
    return [i async for i in async_generator()]
