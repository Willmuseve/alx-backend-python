#!/usr/bin/env python3

"""
a type-annotated function concat that takes a string str1 and a string str2
as arguments and returns a concatenated string
"""


def concat(first_string: str, second_string: str) -> str:
    """
    Concatenating two strings
    """
    new_string = first_string + second_string
    return new_string
