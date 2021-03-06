# encoding: utf-8
def print_iso(str_obs, value):
    print("{}\n\t{}".format(str_obs,value))

def print_json(str_obs, value):
    print("\t{{ \'{}\':{} }}".format(str_obs,value))

def get_hex(obj):
    #in case of list
    if "list" in str(type(obj)):
        l_obj = []
        for x in range(0,len(obj)):
            l_obj.append(format(obj[x], '02X'))
        return l_obj
    #in case of number real or integer
    if "float" or "int" or "double" in str(type(obj)):
        return format(obj, '02X')

def debug_bitmap(value):
    str = ""
    str = str + "0________10________20________30________40________50________60__64\n"
    str = str + "1234567890123456789012345678901234567890123456789012345678901234  n-th bit\n"
    str = str + "{:064b}".format(value)
    return str
    
def bits_to_bitmap(list_bitmap = []):
    bit = 0
    for count in range(0,len(list_bitmap)):
        bit = bit + (1 << 128 - list_bitmap[count])
    return bit

