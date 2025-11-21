"""datakit_lite: helpful utilities for Python and analytics education."""

from .paths import project_paths
from .summary import summarize_table
from .timer import log_duration, timeit

__all__ = [
    "summarize_table",
    "project_paths",
    "timeit",
    "log_duration",
]
