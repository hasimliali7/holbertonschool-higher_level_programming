#!/usr/bin/python3
"""
Bu modul Python obyektini JSON string-ə çevirən funksiyanı ehtiva edir.
"""
import json


def to_json_string(my_obj):
    """
    Python obyektinin JSON təmsilini (string) qaytarır.

    Args:
        my_obj: Serializasiya olunacaq Python obyekti.

    Returns:
        str: Obyektin JSON string forması.
    """
    return json.dumps(my_obj)
