#!/usr/bin/env python3
""" 2. Measure the runtime """
import asyncio
import time
import random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """ Create a measure_time function with integers
    n and max_delay as arguments that measures the total
    execution time for wait_n(n, max_delay),
    and returns total_time / n.
    Your function should return a float. """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
