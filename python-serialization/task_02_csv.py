#!/usr/bin/env python3
"""
Bu modul CSV faylını oxuyub onu JSON formatına çevirən
 funksiyanı ehtiva edir.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    CSV faylındakı məlumatları 'data.json' faylına çevirir.

    Args:
        csv_filename (str): Oxunacaq CSV faylının adı.

    Returns:
        bool: Çevrilmə uğurlu olarsa True, əks halda False.
    """
    try:
        data_list = []
        # CSV faylını açırıq və hər sətri lüğət kimi oxuyuruq
        with open(csv_filename, mode='r', encoding='utf-8') as csv_f:
            csv_reader = csv.DictReader(csv_f)
            for row in csv_reader:
                data_list.append(row)

        # Əldə olunan siyahını JSON formatında 'data.json' faylına yazırıq
        with open('data.json', mode='w', encoding='utf-8') as json_f:
            json.dump(data_list, json_f)

        return True

    except FileNotFoundError:
        # Fayl tapılmadıqda False qaytarırıq
        return False
    except Exception:
        # Digər xətalar zamanı False qaytarırıq
        return False
