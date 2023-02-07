#!/usr/bin/env python3
'''
Defines a coroutine called async_generator
'''
from typing import Iterator
import random
import asyncio


async def async_generator() -> Iterator[int]:
    '''
    Generator function loops to 10
    '''
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
