#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # dir() funksiyası modulun daxilindəki bütün adları siyahı kimi qaytarır
    names = dir(hidden_4)
    
    # Siyahını əlifba sırası ilə düzürük
    names.sort()
    
    for name in names:
        # Şərt: Adlar "__" ilə başlamamalıdır
        if not name.startswith("__"):
            print(name)
