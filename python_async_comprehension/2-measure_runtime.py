#!/usr/bin/env python3
"""
measure_runtime should measure the total runtime and return it.
"""

import asyncio
import time
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime should measure the total runtime and return it.
    """

    start = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = time.time()
    return end - start
