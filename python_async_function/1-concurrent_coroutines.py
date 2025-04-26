#!/usr/bin/env python3
"""
Import wait_random and implement wait_n
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    write an async routine called wait_n that takes in 2 int arguments
    """
    delay = []
    task = []

    for _ in range(n):
        task.append(asyncio.create_task(wait_random(max_delay)))

    for task in asyncio.as_completed(task):
        delays = await task
        delay.append(delays)

    return delay
