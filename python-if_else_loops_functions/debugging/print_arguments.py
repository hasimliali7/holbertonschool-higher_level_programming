#!/usr/bin/python3
import sys

# range funksiyasını 1-dən başladırıq ki, 0-cı indeksdəki fayl adını ötürək
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
