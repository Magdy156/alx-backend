#!/usr/bin/env python3
"""
index range func
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retrieves the index range
    """
    start_index = (page - 1) * page_size
    return (start_index, start_index + page_size)
