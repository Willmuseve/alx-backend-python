#!/usr/bin/env python3
"""A coroutine that takes no arguments
Random Module is used."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that loosp 10 times
    each time asynchronous wait 1 second then yield a
    random number btn 0 and 10.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
