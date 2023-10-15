#!/usr/bin/env python3
""" 3. Tasks """
import asyncio
import concurrent.futures
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay):
    """ Write a function (do not create an async function,
    use the regular function syntax to do this)
    task_wait_random that takes an integer max_delay
    and returns a asyncio.Task. """
    loop = asyncio.get_event_loop()
    executor = concurrent.futures.ThreadPoolExecutor()

    def wait_random_sync(max_delay):
        return loop.run_in_executor(executor, wait_random, max_delay)

    return asyncio.ensure_future(wait_random_sync(max_delay))
