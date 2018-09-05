import random

sock_types = ['ankle','thigh','crew','calf']
my_socks= []
for i in range(100):

    my_socks.append(random.choice(sock_types))
print(my_socks)

for i in range(len(sock_types)):
    count= my_socks.count(sock_types[i])

    # if count%2 == 0:
    #     pair_socks = count/2
    #     extra_socks = 'no'
    # else:
    #     pair_socks = count //2
    #     extra_socks = count%2
    # print(f"{sock_types[i]} socks = {count}")
    # print(f"I have {pair_socks} pair of {sock_types[i]}  of socks and {extra_socks} extra socks" )
    print(f"I have {count//2} pairs of {sock_types[i]} socks")

