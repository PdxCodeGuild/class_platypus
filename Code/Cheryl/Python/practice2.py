#playing around with dictionaries

my_dict = {'key 1': 123, 'key 2': 456, 'key 3': 'A string value'}

my_dict_two = {'key 1': 673, 'key 2': 732, 'a different key': 'A differnt string value'}

for common_key in my_dict.keys() & my_dict_two.keys():
    print(my_dict[common_key], my_dict_two[common_key])


