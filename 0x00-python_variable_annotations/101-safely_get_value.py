#!/usr/bin/env python3

"""
Add type annotation
"""


from typing import TypeVar, Any, Mapping, Union, Optional


X = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default:
        Optional[X] = None) -> Union[Any, X]:
    """
    Retrieve the value from the dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
