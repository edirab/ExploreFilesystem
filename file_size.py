import os
from pprint import pprint


def get_size(start_path = '../'):
    """ Возвращает размер указанного файла или каталога """
    total_size = 0

    if os.path.isfile(start_path):
        return os.path.getsize(start_path)

    elif os.path.isdir(start_path):
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    # print(fp, os.path.getsize(fp))
                    total_size += os.path.getsize(fp)

    return total_size


def get_size_in_dir(abs_path ='C:/Users/corsair/'):
    list_items = os.listdir(abs_path)
    dict_items = {}

    for elem in list_items:
        size_ = get_size(start_path = abs_path + elem)
        dict_items[elem] = size_

    return dict_items


def constrain_file_size(fsize):

    val = fsize
    funits = 'bytes'

    if val >= 2 ** 30:
        fsize /= 2 ** 30
        funits = 'Gib'
    elif 2 ** 20 <= val < 2 ** 30:
        fsize /= 2 ** 20
        funits = 'Mib'
    elif 2 * 10 <= val < 2 ** 20:
        fsize /= 2 ** 10
        funits = 'Kib'
    return fsize, funits
