#lab 10 version 4 MODE


data_list = input('Input your list: ')
for data in data_list:
    data_dict = {}
for data in data_list:
    if data not in data_dict.keys():
        data_dict[data] = 1


data_dict = {}
for data in data_list:
    if data not in data_dict.keys():
        data_dict[data] = 1
    else:
        data_dict[data] += 1



# Another method that works
#
# from statistics import mode

# def data():
#     try:
#         final_data_set = []
#         data_set = input('Please enter your data set. >  ')
#         data_set = data_set.split(',')
#         for i in range(len(data_set)):
#             i = data_set[i].strip(' ')
#             final_data_set.append(i)
#         print(f"MODE of this data set is: {mode(final_data_set)}")
#         return
#     except ValueError:
#         print(f'There is no MODE in this data set: {data_set}')
#
# data()