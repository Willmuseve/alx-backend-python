#!/usr/bin/env python3
"""This program involves an asynchronous coroutine function
that does rando delay with provided values"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function takes in an integer argument max_delay with a
    default value of 10. Wait_Rndom that waits for random delay
    between 0 and max_delay and returns it
    """

    wait_random = random.random() * max_delay

    await asyncio.sleep(wait_random)
    return (wait_random)
