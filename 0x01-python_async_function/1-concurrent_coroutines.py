#!/usr/bin/env python3
'''
Running async coroutine concurrrently to get a sorted array of random floats
'''
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Runs wait_random n times concurrently
    '''
    res = await asyncio.gather(*[wait_random(max_delay) for i in range(n)])
    return res
