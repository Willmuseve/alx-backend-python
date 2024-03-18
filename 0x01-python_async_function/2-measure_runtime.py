#!/usr/bin/env python3
"""Import wait_n to this file.
creates a measure_time function that  measures the total
execution time"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function takes in two integers as arguments that measures the
    total execution time for `wait_n` func with `n` coroutines.
    Params:
        n(int): number of coroutines
        max_delay(int): max amount of delay in seconds (random)
    Returns:
        Approximate elapsed time per coroutine(float)
    time module is used
    """

    time_on = time.time()
    asyncio.run(wait_n(n, max_delay))

    return ((time.time() - time_on) / n)
