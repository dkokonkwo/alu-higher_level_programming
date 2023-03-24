#!/usr/bin/python3
"""creates class that requires specific attribute"""


class LockedClass:
    """states the specific attribute required"""
    __slots__ = ("first_name")
