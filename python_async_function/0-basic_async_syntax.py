#!/usr/bin/env python3
""" """
import asyncio
from typing import Iterable, Sequence, List, Tuple
import random


async def wait_random(max_delay: int = 10) -> float:
    """ """
    delay = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(delay)
    return max_delay
