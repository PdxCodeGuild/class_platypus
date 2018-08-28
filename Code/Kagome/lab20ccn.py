#
#
# def cc_validation(card):
#     for i in range(len(card)):
#         if card < 10:
#             return False
#
# def get_second_num(num):
#     if num > 10:
#         return None
#
# def ccn(ccn_string):
#     if len(ccn_string) != 16:
#         return False
#
#
#     cc = []
#     for i in range(len(card)):
#         if cc[i] > 9:
#             cc[i] -= 9
#         total += cc[i]
#     second_num = get_second_num(total)
#     check_digit = pop.ccn(-1)
#     return second_num == check_digit
#
#     for i in range(0, len(cc), 2):
#         cc[i] *= 2
#     total = 0
#     for i in range(len(cc)):
#         if cc[i] > 9:
#             cc[i] -= 9
#         total += cc[i]
#     second_digit = get_second_num(total)
#     ccn_string.reverse()
#     return second_num == check_digit

# #ccn[i] *= 2

def get_second_digit(num):
    if num < 10:
        return None

#if num not 16 digits then return False
def validate_credit_card(ccn_str):
    if len(ccn_str) != 16:
        return False

    cc = []
    for i in range(len(ccn_str)):
        cc.append(int(ccn_str[i]))

#pop 1, reverse num, double nums
    check_digit = cc.pop(-1)
    cc.reverse()
    for i in range(0, len(cc), 2):
        cc[i] *= 2
    total = 0
    for i in range(len(cc)):
        if cc[i] > 9:
            cc[i] -= 9
        total += cc[i]
    second_digit = get_second_digit(total)
    return second_digit == check_digit


credit_card_str = input('enter your credit card: ')
print(validate_credit_card(credit_card_str))
