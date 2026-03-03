#!/usr/bin/python3
"""
Bu modul bir mətn faylını oxuyan funksiyanı ehtiva edir.
"""


def read_file(filename=""):
    """
    UTF8 formatında olan mətn faylını oxuyur və stdout-a çap edir.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
