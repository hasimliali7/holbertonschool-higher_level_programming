#!/usr/bin/python3
"""
Bu modul fayla mətn əlavə edən funksiyanı ehtiva edir.
"""


def append_write(filename="", text=""):
    """Mətni faylın sonuna əlavə edir və simvol sayını qaytarır."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
