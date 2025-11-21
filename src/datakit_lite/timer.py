"""Timer utilities for measuring function and code block execution time.

This module provides:
- timeit: decorator for timing function execution
- log_duration: context manager for timing code blocks
"""

from contextlib import contextmanager
from functools import wraps
import time


def timeit(fn):
    """Print how long a function takes.

    Parameters:
    ----------
    fn : callable
        The function to be timed.
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        duration = round(end - start, 4)
        print(f"{fn.__name__} took {duration} seconds")
        return result

    return wrapper


@contextmanager
def log_duration(label: str):
    """Context manager that prints how long a block takes."""
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    duration = round(end - start, 4)
    print(f"{label} took {duration} seconds")
