#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for idx in my_list:
        if idx == search:
            my_list[my_list.index(search)] = replace
    return my_list
