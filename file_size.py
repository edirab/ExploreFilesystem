import os
import json
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


def explore_dir(abs_path ='C:/Users/corsair/'):
    """Для заданного каталога вычисляет имена, веса подкаталогов и их даты модификации.
    Полученные данные записывает в файл с именем 'abs_Paths'"""
    rescan = False

    dict_items = {}
    dict_subelems = {}
    dict_items[abs_path] = dict_subelems

    file_name = abs_path.replace(":", "")
    file_name = file_name.replace("/", "_")
    print("Searching for ", file_name, "...\n")

    prev_data = None
    try:
        prev_data_file = open(file_name)
        prev_data = json.loads(prev_data_file.read())
    except FileNotFoundError:
        print("File ", file_name, " not found. Scannig...\n")

    list_items = os.listdir(abs_path)
    #print(list_items)

    if prev_data is not None:
        # print("Raw read from file: ", prev_data)

        set_list_items = set(list_items)
        list_times = [os.path.getmtime(abs_path + elem) for elem in list_items]
        set_time_ = set(list_times)

        set_prev_data_items = {k for k in prev_data[abs_path].keys()}
        # print("Prev data dirs set: ", set_prev_data_items)
        # print("Curr data dirs set: ", set_list_items)

        set_prev_data_times = {t[1] for t in prev_data[abs_path].values()}
        # print("Prev data dirs times: ", set_prev_data_times)
        # print("Curr data dirs times: ", set_time_)

        if (set_prev_data_items == set_list_items) and (set_prev_data_times == set_time_):
            print("Everything is up to date")
            return prev_data
        else:
            rescan = True
    else:
        rescan = True

    if rescan:
        for elem in list_items:
            size_ = get_size(start_path = abs_path + elem)
            time_ = os.path.getmtime(abs_path + elem)
            dict_subelems[elem] = (size_, time_)

        file = open(file_name, 'w')
        file.write(json.dumps(dict_items))
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


def pretty_print_info(dict_items):
    dirs = []
    for key, val in dict_items.items():
        pos = key.rfind(".")
        if pos != -1:
            file_ext = key[pos + 1:].lower()

            f_size, f_units = constrain_file_size(val[0])
            print(key[:22].ljust(25), file_ext.ljust(7), str(f_size)[:5].ljust(6), f_units)
        else:
            dirs.append(key)

    print('-' * (25 + 1 + 7 + 1 + 6 + 1 + 3))

    for elem in dirs:
        val = dict_items[elem][0]
        f_size, f_units = constrain_file_size(val)

        print(elem[:22].ljust(25), 'dir'.ljust(7), str(f_size)[:5].ljust(6), f_units)
