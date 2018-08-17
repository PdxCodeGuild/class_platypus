# def is_even(a):
#     if type(a) is int:
#         return a % 2 == 0
#     else:
#         return -1


def double(s):
    out_string = ''
    for i in s:
        out_string = out_string + i * 2
    return out_string