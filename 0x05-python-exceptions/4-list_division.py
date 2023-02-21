#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    newlist=[]
    div=0
    for i in range(list_length):
        try:
            newlist.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            newlist.append(0)
            continue
        except IndexError:
            print("division out of range")
            newlist.append(0)
            continue
        except ZeroDivisionError:
            print("division by 0")
            newlist.append(0)
            continue
        finally:
            # newlist.append(div)
            pass
        
    return newlist

if __name__ == '__main__':

    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

