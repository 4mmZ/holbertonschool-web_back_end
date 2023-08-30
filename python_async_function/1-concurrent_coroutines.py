#!/usr/bin/env python3
"" ""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import Iterable, Sequence, List, Tuple
import random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """ """
    coroutine_list = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutine_list)
    return results
