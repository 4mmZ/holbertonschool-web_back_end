#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async """
import asyncio
from typing import Iterable, Sequence, List, Tuple
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Import wait_random from the previous
    python file that you’ve written and write an async routine
    called wait_n that takes in 2 int arguments
    (in this order): n and max_delay.
    You will spawn wait_random n times
    with the specified max_delay. """
    results = []

    async def wait_and_append(delay: int):
        result = float(await wait_random(max_delay))
        results.append(result)

    await asyncio.gather(*(wait_and_append(i) for i in range(n)))
    return results
