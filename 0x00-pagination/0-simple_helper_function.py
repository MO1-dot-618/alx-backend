#!/usr/bin/env python3
from typing import Tuple
"""
function file
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ function """
    return (((page - 1) * page_size, page * page_size))
