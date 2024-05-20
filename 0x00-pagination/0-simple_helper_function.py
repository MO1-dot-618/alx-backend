#!/usr/bin/env python3
"""
function file here
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ function that shows range """
    return (((page - 1) * page_size, page * page_size))
