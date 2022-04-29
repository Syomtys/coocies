import re
import os

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


with open(filename, "r", encoding='utf-8') as file:
    file_str = file.read()
    final_str = cleaning(file_str)
    file.write(final_str)
