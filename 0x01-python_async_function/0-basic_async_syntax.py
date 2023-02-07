#!/usr/bin/env python3
'''
Asynchronous coroutine waits for a random delay between 0 and max_delay
'''
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    '''
    Max delay function
    '''
    random_duration = random.uniform(0, max_delay)
    time.sleep(random_duration)
    return random_duration
