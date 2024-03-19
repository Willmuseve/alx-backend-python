#!/usr/bin/env python3
"""Coroutine called async_comprehension that takes no arguments
and.
asunc_generator is imported from the previous task"""

from typing import List
from importlib import import_module as i

async_generator = i('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutin collects random numbers using async comprehensing over
    async_generator, then return 10 random numbers.
    """

    return [num async for num in async_generator()]
