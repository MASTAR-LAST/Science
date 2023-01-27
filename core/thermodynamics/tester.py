"""
"""

from decimal import Decimal
from typing import Union
from time import time

def speedTest(func):
    def testing(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Running time is {end-start}")
        return result

    return testing