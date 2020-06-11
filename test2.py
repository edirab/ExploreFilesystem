import file_size
from pprint import pprint

path = "D:/PycharmProjects/"
path = "C:/Program Files/"

items = file_size.explore_dir(path)

print("**********************************")
pprint(items)

file_size.pretty_print_info(items[path])