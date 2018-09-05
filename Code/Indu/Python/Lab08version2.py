# Simple calculator
#created by Indu Thekkemeppilly Sivakumar in 08/14/2018
operation_list = ['addition','subtraction','multiplication','division']
while True:
    print("The available operations are addition,subraction,multiplication,division")
    operation = input("What is the operation you would like to perform? \n")
    firstnum = float(input("What is the first number?\n"))
    secondtnum = float(input("What is the second number?\n"))
    #print(firstnum+secondtnum)
    if operation == 'addition':
        print(f"{firstnum}+{secondtnum} is {(firstnum+secondtnum)}")
    elif operation == 'subtraction':
        print(f"{firstnum}-{secondtnum} is {(firstnum-secondtnum)}")
    elif operation == 'multiplication':
        print(f"{firstnum} x {secondtnum} is {(firstnum*secondtnum)}")
    elif operation == 'division':
        print(f"{firstnum}/{secondtnum} is {(firstnum/secondtnum)}")
    repeat = input("Do you want to perfom another operation")
    if repeat =='no':
        break