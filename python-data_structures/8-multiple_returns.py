#!/usr/bin/python3
def multiple_returns(sentence):
    # Uzunluğu hesablayırıq
    length = len(sentence)
    
    # Əgər string boşdursa, ilk simvol None olmalıdır
    if length == 0:
        first_char = None
    else:
        first_char = sentence[0]
        
    # Tuple şəklində qaytarırıq
    return (length, first_char)
