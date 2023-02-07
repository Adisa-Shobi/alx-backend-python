#!/usr/bin/env python3
'''
Running async coroutine concurrrently to get a sorted array of random floats
'''
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Runs wait_random n times concurrently
    '''
    res = await asyncio.gather(
        *[task_wait_random(max_delay) for i in range(n)]
    )
    return res
