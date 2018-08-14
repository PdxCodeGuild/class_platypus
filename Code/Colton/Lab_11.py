while True:
    op = str(input("What operation do you want to perform? "))
    operation_list = ['-', '+', '/', '*']
    if op not in operation_list:
        print("Not a valid operation")
        continue
    f_num = float(input("What is the first number? "))
    s_num = float(input("What is the second number "))
    if op == '+':
        print(f_num + s_num)
    elif op == '-':
        print(f_num - s_num)
    elif op == '/':
        print(f_num / s_num)
    elif op == '*':
        print(f_num * s_num)
    end = input("again? ")
    if end != "yes":
        break