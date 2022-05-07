import re
import os

final_str = ''
script_mod = 0
# 1 - ввод имени файла из папки кукиес и отчистка его
# 0 - чек всех файлов и отчистка

def cleaning(string):
    string = re.sub(r"(,([\{])[^\{}]+(microsoft)[^\{}]+[\}])", '', string, flags=re.M)
    print(' - clean - microsoft')
    string = re.sub(r"(,([\{])[^\{}]+(paypal)[^\{}]+[\}])", '', string, flags=re.M)
    print(' - clean - paypal')
    string = re.sub(r"(,([\{])[^\{}]+(cnn)[^\{}]+[\}])", '', string, flags=re.M)
    print(' - clean - cnn')
    string = re.sub(r"(,([\{])[^\{}]+(hotmail)[^\{}]+[\}])", '', string, flags=re.M)
    print(' - clean - hotmail')
    string = re.sub(r"(,([\{])[^\{}]+(ads)[^\{}]+[\}])", '', string, flags=re.M)
    print(' - clean - ads')
    string = re.sub(r"(,([\{])[^\{}]+(google)[^\{}]+[\}])", '', string, flags=re.M)
    print(' - clean - google')
    string = re.sub(r"(,([\{])[^\{}]+(outlook)[^\{}]+[\}])", '', string, flags=re.M)
    print(' - clean - outlook')
    string = re.sub(r"(,([\{])[^\{}]+(live)[^\{}]+[\}])", '', string, flags=re.M)
    print(' - clean - live')
    string = re.sub(r"(,([\{])[^\{}]+(facebook)[^\{}]+[\}])", '', string, flags=re.M)
    print(' - clean - facebook')
    string = re.sub(r"(,([\{])[^\{}]+(youtube)[^\{}]+[\}])", '', string, flags=re.M)
    print(' - clean - youtube')
    string = re.sub(r"(,([\{])[^\{}]+(gmail)[^\{}]+[\}])", '', string, flags=re.M)
    print(' - clean - gmail')
    string = re.sub(r"(,([\{])[^\{}]+(instagram)[^\{}]+[\}])", '', string, flags=re.M)
    print(' - clean - instagram')
    string = re.sub(r"(,([\{])[^\{}]+(meta)[^\{}]+[\}])", '', string, flags=re.M)
    print(' - clean - meta')
    final_str = string
    return (final_str)


if script_mod == 1:
    filename = 'coocies/'+input()+'.txt'
    print(filename)
    with open(filename, "r+", encoding='utf-8') as file:
        file_str = file.read()
        final_string = cleaning(file_str)
        file.seek(0)
        file.write(final_string)
        file.truncate()

if script_mod == 0:

    if not(os.path.isfile('coocies_list.txt')):
        text_file = open("coocies_list.txt", "w")
        print('create - coocies_list.txt')

    CaputalList = {}

    for dirpath, dirnames, filenames in os.walk('./coocies/'):
        path_files = []
        for filename in filenames:
            text = str(os.path.join(dirpath, filename)).replace('\\', '/')
            path_files.append(text)
            dir_name = text.split('/')[-2]
            if text != './coocies/.DS_Store':
                CaputalList[dir_name] = path_files
                filename = text
                text_coocies = ''
                with open(filename, "r+", encoding='utf-8') as file:
                    file_str = file.read()
                    print('')
                    print('------')
                    print('clean - '+filename)
                    text_coocies = cleaning(file_str)
                with open('coocies_list.txt', "r+", encoding='utf-8') as file:
                    file_str = file.read()
                    file_str = file_str+text_coocies
                    file.seek(0)
                    file.write(file_str)
                    file.truncate()
                    col = 1
                    col = col + 1
                    print('coocies - ' + str(col))

    with open('coocies_list.txt', "r+", encoding='utf-8') as file:
        file_str = file.read()
        final_string = re.sub(r"(\}\]\[\{)", '},{', file_str, flags=re.M)
        print('')
        print('')
        print(' - gluing сoocios')
        file.seek(0)
        file.write(final_string)
        file.truncate()


    #print(CaputalList)