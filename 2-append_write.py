#!/usr/bin/python3
"""
Bu modul bir faylın sonuna mətn əlavə edən funksiyanı ehtiva edir.
"""


def append_write(filename="", text=""):
    """
    Mətni UTF8 formatında faylın sonuna əlavə edir.

    Args:
        filename (str): Faylın adı.
        text (str): Əlavə olunacaq mətn.

    Returns:
        int: Əlavə olunmuş simvolların sayı.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
