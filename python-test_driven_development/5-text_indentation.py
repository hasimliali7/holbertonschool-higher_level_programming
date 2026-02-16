#!/usr/bin/python3
"""
This module provides a function that indents text.
It adds two new lines after each '.', '?', and ':' characters.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Mətnin əvvəlindəki və sonundakı tam boşluqları təmizləyirik
    # Lakin daxili boşluqları qorumalıyıq
    
    chars = ['.', '?', ':']
    i = 0
    
    # Başlanğıcdakı boşluqları keçirik
    while i < len(text) and text[i] == ' ':
        i += 1
        
    while i < len(text):
        print(text[i], end="")
        if text[i] in chars:
            print("\n")
            i += 1
            # İşarədən sonra gələn bütün boşluqları keçirik
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
