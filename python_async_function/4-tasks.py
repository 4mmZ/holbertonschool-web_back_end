#!/usr/bin/env python3
""" 4. Tasks """
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """ Take the code from wait_n and
    alter it into a new function task_wait_n.
    The code is nearly identical to wait_n
    except task_wait_random is being called. """
    delay_list = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        delay_list.append(delay)

    return sorted(delay_list)
