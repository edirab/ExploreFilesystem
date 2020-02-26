import file_size


dict_items = file_size.get_size_in_dir('E:/University/9sem/')
dirs = []

for key, val in dict_items.items():
    pos = key.rfind(".")
    if pos != -1:
        file_ext = key[pos + 1:].lower()

        f_size, f_units = file_size.constrain_file_size(val)
        print(key[:22].ljust(25), file_ext.ljust(7), str(f_size)[:5].ljust(6), f_units)
    else:
        dirs.append(key)

print('-' * (25 + 1 + 7 + 1 + 6 + 1 + 3))

for elem in dirs:
    val = dict_items[elem]
    f_size, f_units = file_size.constrain_file_size(val)

    print(elem[:22].ljust(25), 'dir'.ljust(7), str(f_size)[:5].ljust(6), f_units)
