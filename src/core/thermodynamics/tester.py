"""
Tesing Unit
===========
This file is contan some of testing tools That can be usfull for
a developers who make this library.

Tools
-----
    `speedTest:`
        This tool is created to calclate a run time for a functions.
                                Time clalclation --> Run time for function + Run time for itself.
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