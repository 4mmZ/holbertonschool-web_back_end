#!/usr/bin/env python3
""" 0. The basics of async """
import asyncio
from typing import Iterable, Sequence, List, Tuple
import random


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that waits
    for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it. """
    delay = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(delay)
    return max_delay
