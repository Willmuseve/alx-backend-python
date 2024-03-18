#!/usr/bin/env python3
"""Imports wait_random from 0-basic_async_syntax.py
write new async routine wait_n that takes in two args"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    New async routine that takes in two args.  `n`
    with the specified `max_delay`
    Returns:
        list of all delays (float values) in ascending order
        without using sort() because of concurrency
    """

    wait_n = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )

    return (sorted(wait_n))
