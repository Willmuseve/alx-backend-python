#!/usr/bin/env python3
"""Import async comprehension from 1-async_comprehension and write
a measure_runtime coroutine."""

import asyncio
import time
from importlib import import_module as i

async_comprehension = i('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures total runtime and return it.
    """

    start_t = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return (time.time() - start_t)
