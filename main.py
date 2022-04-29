import re
import os

final_str = ''

filename = input()

def cleaning(string):
    string = re.sub(r"(,([\{])[^\{}]+(microsoft)[^\{}]+[\}])", '', string, flags=re.M)
    string = re.sub(r"(,([\{])[^\{}]+(google)[^\{}]+[\}])", '', string, flags=re.M)
    string = re.sub(r"(,([\{])[^\{}]+(outlook)[^\{}]+[\}])", '', string, flags=re.M)
    string = re.sub(r"(,([\{])[^\{}]+(live)[^\{}]+[\}])", '', string, flags=re.M)
    string = re.sub(r"(,([\{])[^\{}]+(facebook)[^\{}]+[\}])", '', string, flags=re.M)
    string = re.sub(r"(,([\{])[^\{}]+(youtube)[^\{}]+[\}])", '', string, flags=re.M)
    string = re.sub(r"(,([\{])[^\{}]+(gmail)[^\{}]+[\}])", '', string, flags=re.M)
    string = re.sub(r"(,([\{])[^\{}]+(instagram)[^\{}]+[\}])", '', string, flags=re.M)
    string = re.sub(r"(,([\{])[^\{}]+(meta)[^\{}]+[\}])", '', string, flags=re.M)
    final_str = string
    return (final_str)


with open(filename, "r+", encoding='utf-8') as file:
    file_str = file.read()
    print(file_str)
    final_string = cleaning(file_str)
    file.seek(0)
    file.write(final_string)
    file.truncate()
