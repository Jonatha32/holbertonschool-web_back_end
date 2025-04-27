#!/usr/bin/env python3
""""
Create a task_wait_n
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """"
     The code is nearly identical to wait_n except task_wait_random
    """
    task = [task_wait_n(max_delay) for _ in range(n)]
    delay = []

    for completed in asyncio.as_completed(task):
        delays = await completed
        delay.append(delays)

    return delay
