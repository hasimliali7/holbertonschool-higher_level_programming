#!/usr/bin/env python3
"""
Bu modul Python lüğətlərini XML formatına çevirmək və
 XML-dən lüğətə qaytarmaq üçün funksiyaları ehtiva edir.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Python lüğətini XML formatında fayla yazır.

    Args:
        dictionary (dict): Serializasiya olunacaq lüğət.
        filename (str): Çıxış XML faylının adı.
    """
    # Kök (root) elementi yaradırıq <data>
    root = ET.Element("data")

    # Lüğətdəki hər bir açar/dəyər cütü üçün alt elementlər əlavə edirik
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # XML ağacını (tree) yaradırıq və fayla yazırıq
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    XML faylından məlumatı oxuyur və Python lüğətinə çevirir.

    Args:
        filename (str): Giriş XML faylının adı.

    Returns:
        dict: Deserializasiya olunmuş lüğət.
    """
    try:
        # XML faylını analiz (parse) edirik
        tree = ET.parse(filename)
        root = tree.getroot()

        # Elementləri yenidən lüğət strukturuna yığırıq
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict

    except FileNotFoundError:
        return None
    except Exception:
        return None
