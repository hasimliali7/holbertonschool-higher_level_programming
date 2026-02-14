#!/usr/bin/python3
def max_integer(my_list=[]):
    # Siyahı boşdursa None qaytarırıq
    if not my_list:
        return None
    
    # İlk elementi max kimi götürürük
    biggest = my_list[0]
    
    # Bütün elementləri müqayisə edirik
    for x in my_list:
        if x > biggest:
            biggest = x
            
    return biggest
