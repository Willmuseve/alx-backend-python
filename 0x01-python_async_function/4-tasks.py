#!/usr/bin/env python3
"""Takes the code from wait_n and alter it to a new
function task_wait_n"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function alters code from `wait_n` into this function.
    Waits for random amounts of time up to `max_delay` This func is
    nearly idential to wait_n except rask_wait_n is being ca,,ed
    Returns:
        list of Task objects, sorted in ascending order
    """

    wait_t = await asyncio.gather(
            *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )

    return (sorted(wait_t))
