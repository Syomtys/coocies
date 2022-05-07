import re
import os
import random


with open('coocies_list.txt', "r+", encoding='utf-8') as file:
    file_str = file.read()
    final_string = re.split(r"\}\,\{", file_str)
    #final_string = re.findall(r"(,([\{])[^\{}]+[^\{}]+[\}])", file_str)
    # for one_coccie in final_string:
    #     one_coccie = re.find(r"(,([\{])[^\{}]+[^\{}]+[\}])", file_str)
    print('max coocies - '+str(len(final_string)))
    num = (len(final_string))
    print('send number coocies ( max '+str(num)+' )')
    user_num = int(input())

    if (os.path.isfile('new_coocies.txt')):
        os.remove('new_coocies.txt')
        text_file = open("new_coocies.txt", "w")
        print('remove and create - new_coocies.txt')
    else:
        text_file = open("new_coocies.txt", "w")
        print('create - new_coocies.txt')

    for i in range(user_num):
        rand = random.randint(0,num)
        print(rand)
        print(final_string[rand])
        with open('new_coocies.txt', "r+", encoding='utf-8') as file:
            file_str = file.read()
            file_str = file_str + '{'+final_string[rand]+'},'
            file.seek(0)
            file.write(file_str)
            file.truncate()

    with open('new_coocies.txt', "r+", encoding='utf-8') as file:
        file_str = file.read()
        file_str = '[' + file_str[:-1] + ']'
        file.seek(0)
        file.write(file_str)
        file.truncate()

