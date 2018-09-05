cc_num = input("Enter number." )
cc_num = list(cc_num)
cc_num = [int(x) for x in cc_num]
check = cc_num.pop()
cc_num.reverse()
cc_num = [2*cc_num[i] if i%2 == 0 else cc_num[i] for i in range(len(cc_num))]
cc_num = [cc_num[i] - 9 if cc_num[i] > 9 else cc_num[i] for i in range(len(cc_num))]
cc_num = sum(cc_num)
cc_num = str(cc_num)
check = str(check)
if cc_num[1] == check:
    print("valid")
else:
    print("invalid")