#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_ = list()
    for j in range(list_length):
        try:
            list_.append(my_list_1[j] / my_list_2[j])
        except ZeroDivisionError:
            list_.append(0)
            print("division by 0")
            continue
        except IndexError:
            list_.append(0)
            print("out of range")
            continue
        except TypeError:
            list_.append(0)
            print("wrong type")
            continue
        finally:
            pass
    return list_
