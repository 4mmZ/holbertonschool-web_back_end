#!/usr/bin/env python3
"" ""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import Iterable, Sequence, List, Tuple
import random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """ """
    results = []
    
    async def wait_and_append(delay: int):
        result = await wait_random(max_delay)
        results.append(result)
    
    await asyncio.gather(*(wait_and_append(i) for i in range(n)))
    return results
