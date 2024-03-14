#!/usr/bin/env python3

"""
a type-annotated function concat that takes a string str1 and a string str2
as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenating two strings.
    Args:
        str1 (str): Egg
        str2 (str): shell
    """
    str3 = str1 + str2
    return str3
